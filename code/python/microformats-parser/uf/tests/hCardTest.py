from uf import hCard

import unittest

class hCardTestCase(unittest.TestCase):
    def setUp(self):
        self.hcard_valid = """<div class="vcard">
  <a class="fn org url" href="http://www.commerce.net/">CommerceNet</a>
  <div class="adr">a
    <span class="type">Work</span>:
    <div class="street-address">169 University Avenue</div>
    <span class="locality">Palo Alto</span>,
    <abbr class="region" title="California">CA</abbr>
    <span class="postal-code">94301</span>
    <div class="country-name">USA</div>
  </div>
  <div class="tel">
   <span class="type">Work</span> +1-650-289-4040
  </div>
  <div class="tel">
    <span class="type">Fax</span> +1-650-289-4041
  </div>
  <div>Email:
   <span class="email">info@commerce.net</span>
  </div>
</div>"""

        self.parser = hCard()

    def test_valid_hcard(self):
        vcard = self.parser.parse(self.hcard_valid)
#        vcard.prettyPrint()
        url = vcard.contents['url'][0].value
        fn = vcard.contents['fn'][0].value
        email = vcard.contents['email'][0].value
        tel = vcard.contents['tel'][0].value
        self.assertEqual(u'http://www.commerce.net/', url)
        self.assertEqual(u'CommerceNet', fn)
        self.assertEqual(u'info@commerce.net', email)

if __name__ == '__main__':
    unittest.main()
