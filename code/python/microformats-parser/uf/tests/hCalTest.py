from uf import hCal

import unittest

class hCalTestCase(unittest.TestCase):
    def setUp(self):
        self.hcal_valid = """<div class="vevent">
    <a class="url" href="http://www.web2con.com/">http://www.web2con.com/</a>
    <span class="summary">Web 2.0 Conference</span>: 
    <abbr class="dtstart" title="2007-10-05">October 5</abbr>-
    <abbr class="dtend" title="2007-10-20">19</abbr>,
    at the <span class="location">Argent Hotel, San Francisco, CA</span>
    </div>
    """
        self.parser = hCal()

    def test_valid_hcal(self):
        vcal = self.parser.parse(self.hcal_valid)
        #print vcal.contents['vevent'][0].__dict__
        self.assertEqual("http://www.web2con.com/", vcal.contents['vevent'][0].contents['url'][0].value)
        self.assertEqual("Web 2.0 Conference", vcal.contents['vevent'][0].contents['summary'][0].value)
        self.assertEqual("Argent Hotel, San Francisco, CA", vcal.contents['vevent'][0].contents['location'][0].value)

if __name__ == '__main__':
    unittest.main()
