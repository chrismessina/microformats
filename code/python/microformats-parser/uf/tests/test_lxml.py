from lxml import etree
import vobject

hcard = """<div class="vcard">
  <a class="fn org url" href="http://www.commerce.net/">CommerceNet</a>
  <div class="adr">
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

hcard2 = """<td class="thumb vcard author">
              <a href="http://twitter.com/aconbere" class="url"><img alt="Anders" class="photo fn" id="profile-image" src="http://s3.amazonaws.com/twitter_production/profile_images/19791522/anders_normal.jpg" /></a>
        </td>"""


html = etree.HTML('./hcard.html')
xsl_doc = etree.parse('./xhtml2vcard.xsl')
transform = etree.XSLT(xsl_doc)
vcard = transform(html)
v = vobject.readOne(str(vcard))
print v
