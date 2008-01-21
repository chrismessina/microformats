from uf import RelTag

import unittest

class RelTagTestCase(unittest.TestCase):
    def setUp(self):
        self.reltag_valid = """<a href="http://anders.conbere.org" rel="tag">Anders Conbere</a>"""
        self.reltag_invalid = """<a href="http://anders.conbere.org" rel="contact colleague something">Anders Conbere</a>"""
        self.parser = RelTag()
    
    def test_get_properties(self):
        output = self.parser.parse(self.reltag_valid)
        self.assertEqual([u'http://anders.conbere.org'], output['tag'])

if __name__ == '__main__':
    unittest.main()