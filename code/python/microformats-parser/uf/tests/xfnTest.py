from uf import XFN

import unittest

class XFNTestCase(unittest.TestCase):
    def setUp(self):
        self.xfn_invalid = """<a href="http://anders.conbere.org" rel="tag">Anders Conbere</a>"""
        self.xfn_valid = """<a href="http://anders.conbere.org" rel="contact colleague something">Anders Conbere</a>"""
        self.parser = XFN()
    
    def test_get_properties(self):
        output = self.parser.parse(self.xfn_valid)
        self.assertEqual({'contact': [u'http://anders.conbere.org'], 'colleague': [u'http://anders.conbere.org']}, output)

if __name__ == '__main__':
    unittest.main()