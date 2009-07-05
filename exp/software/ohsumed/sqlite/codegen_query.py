
# generates query.sql for passing to sqlite3 for searching

def fix(s):
  s = s.replace('"', '""').replace("'", "''").replace(",", " ").replace("-", " ")
  return " OR ".join(s.split())

o = open("query.sql", "w")
o.write(".separator ' '\n")

for line in open("../queries.txt", "r"):
  query = line.strip()
  fixed = fix(query)
  o.write("SELECT '%s', docid FROM ohsumed WHERE content MATCH '%s' LIMIT 10;\n" % (query, fixed))

o.close()
