
# generates build.sql which is passed to sqlite3 for indexing

def sanitize(s):
  return s.replace('"', '""').replace("'", "''").strip()

o = open("build.sql", "w")
o.write("PRAGMA synchronous = off;\n")
o.write("CREATE VIRTUAL TABLE ohsumed USING fts3;\n")
o.write("BEGIN;\n")

for line in open("../ohsumed.flat", "r"):
  docidstr, text = line.strip().split("\t")
  o.write("INSERT INTO ohsumed (docid, content) VALUES (%d, \"%s\");\n" % (int(docidstr), sanitize(text)))

o.write("COMMIT;")
o.close()
