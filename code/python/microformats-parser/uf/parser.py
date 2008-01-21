from lxml import etree
from BeautifulSoup import BeautifulSoup
import filters
import vobject
import sys
import os

def get_abs_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

class Parser(object):
    def _open_stream(self, source):
        if hasattr(source, 'read'):
            stream = source.read()
        else:
            if isinstance(source, unicode):
                stream = source.encode('utf-8')
            elif isinstance(source, str):
                stream = source
            else:
                stream = str(source)
        return stream

class XHTMLParser(Parser):
    filters = []

    def parse(self, stream):
        return self.run_filters(self._transform(self._open_stream(stream)))

    def add_filter(self, filter):
        self.filters.append(filter)

    def run_filters(self, input):
        def _run_filters(filters, input):
            while filters:
                filter = filters.pop()
                return _run_filters(filters, filter(input)) 
            return input
        return _run_filters(self.filters, input)

    def _transform(self, stream):
        input = etree.HTML(self._open_stream(stream))
        xsl = etree.parse(self.xsl_file)
        transform = etree.XSLT(xsl)
        output = transform(input)
        return output

    def _open_stream(self, source):
        if hasattr(source, 'read'):
            stream = source.read()
        else:
            if isinstance(source, unicode):
                stream = source.encode('utf-8')
            elif isinstance(source, str):
                stream = source
            else:
                stream = str(source)
        return stream

class vObjParser(XHTMLParser):
    def __init__(self):
        super(Parser, self).__init__()
        self.add_filter(filters.to_vobject)
        self.add_filter(filters.to_str)

class hCard(vObjParser):
    xsl_file = get_abs_path("./xsl/xhtml2vcard.xsl")

class hCal(vObjParser):
    xsl_file = get_abs_path("./xsl/xhtml2vcal.xsl")

class hAtom(XHTMLParser):
    xsl_file = get_abs_path("./xsl/hAtom2Atom.xsl")

    def __init__(self):
        super(Parser, self).__init__()
        self.add_filter(filters.atom2python)
        self.add_filter(filters.to_str)

class LinkParser(Parser):
    """
    URLParsers uses the rel attribute to assign meta data to the urls.
    This is the parent class of XFNParser and RelTagParser
    """
    properties = set()

    # it would be nice to be able to send in a Beautiful SoupStrainer
    # so we don't parse the whole page everytime
    def parse(self, stream):
        # self.path = path
        # self.source = fetch(path)
        return self.get_links(self._transform(self._open_stream(stream)))
    
    def _transform(self, stream):
        return BeautifulSoup(self._open_stream(stream))

    def attr_filter(self, prop):
        """
        a factory for creating attribute filters.
        Used to figure out if a tag has particular attribute values.
        """
        return lambda attr: attr is not None\
            and prop in attr.split(' ')

    def attr_not_empty_filter(self):
        """
        a factory for creating a filter to test
        if an element has a particular arrtibute
        """
        return lambda attr: attr is not None\
            and attr is not ""

    def get_links_with_property(self, soup, prop):
        """
        returns urls with certain rel values
        """
        return soup.findAll('a', {'rel': self.attr_filter(prop), 'href': self.attr_not_empty_filter()})
    
    def get_links(self, soup):
        """
        returns a dictionary where the keys are properties of the spec
        and the values are lists of urls that were founds for that.
        """
        links = {}

        for prop in self.properties:
            retrieved_links = self.get_links_with_property(soup, prop)
            links[prop] = []
            
            for link in retrieved_links:
                links[prop].append(link.get('href'))

            if links[prop] == []:
                del links[prop]
        return links

class XFN(LinkParser):
    """
    XFNParser is a link parser that looks for rel attributes in the list of
    approved propererties for xfn.
    """
    
    properties = set(['me', 'contact', 'acquaintance', 'friend',
                  'met', 'co-worker', 'colleague',
                  'co-resident', 'neighbor', 'child',
                  'parent', 'sibling', 'spouse', 'kin',
                  'muse', 'crush', 'date', 'sweatheart',
                  ])

    def get_rels_me(self):
        return get_links_with_property('me')

class RelTag(LinkParser):
    """
    Very simple extension of the LinkParser class, returns a list of urls that matched
    the rel="tag" attribute
    """
    
    properties = set(['tag'])