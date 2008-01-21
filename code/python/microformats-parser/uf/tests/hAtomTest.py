from uf import hAtom

import unittest

class hAtomTestCase(unittest.TestCase):
    def setUp(self):
        self.hatom_valid = """<div id="content">
 <h2 id="home-title">
  Latest microformats news 
  <a href="http://www.microformats.org/feed/" title="link to RSS feed" id="feed-link">
   <img src="/img/xml.gif" width="23" height="13" alt="XML" />
  </a>
 </h2>

 <div class="entry">
  <h3 id="post-60">
   <a href="http://www.microformats.org/blog/2005/...">Wiki Attack</a>
  </h3>
  ...
 </div>

 <div class="entry">
  <h3 id="post-59">
   <a href="http://www.microformats.org/blog/2005/...">Web Essentials Audio</a>
  </h3>
  ...
 </div>

 <div class="entry">
  <h3 id="post-57">
   <a href="http://www.microformats.org/blog/2005/...">WebZine FollowUp</a>
  </h3>
  ...
 </div>
</div>
"""
        self.parser = hAtom()

    def test_valid_hatom(self):
        atom = self.parser.parse(self.hatom_valid)
        print atom.entries

if __name__ == '__main__':
    unittest.main()
