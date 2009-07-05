
# generates build.trec data file for zettair's indexing utility

out = open("build.trec", "w")
for line in open("../ohsumed.flat", "r"):
  docidstr, text = line.strip().split("\t")
  out.write("<DOC><DOCNO>%s</DOCNO><TEXT>%s</TEXT></DOC>\n" % (docidstr, text))
out.close()
