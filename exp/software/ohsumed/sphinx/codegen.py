
# generates build.xml for sphinx indexing

from xml.sax.saxutils import escape

def sanitize(l):
  s = ""
  for ch in escape(l.strip()):
    i = ord(ch)
    if i < 32 or i > 126:
      s += hex(i)
    else:
      s += ch
  return s

o = open("build.xml", "w")

o.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
o.write("<sphinx:docset>")
o.write("<sphinx:schema>")
o.write("<sphinx:field name=\"content\"/>")
o.write("</sphinx:schema>")

for line in open("../ohsumed.flat", "r"):
  docidstr, text = line.strip().split("\t")
  o.write("<sphinx:document id=\"%s\"><content>%s</content></sphinx:document>\n" % (docidstr, sanitize(text)))

o.write("</sphinx:docset>")
o.close()
