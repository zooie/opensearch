
# converts batch.txt (stdout of zettair multisearch)
# to results.txt (format: query_text\wdocid\n) for passing to scorer.py

results = []
current = []

for line in open("batch.txt", "r"):
  if line.find("docid") > 0:
    current.append(line.split()[1])
  elif len(current) == 10:
    results.append(current)
    current = []

out = open("results.txt", "w")
for line, rset in zip(open("../queries.txt", "r"), results):
  q = line.strip()
  for r in rset:
    out.write(q + " " + r + "\n")
out.close()
