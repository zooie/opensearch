
# output format: query\n

d = {}
topicid = None

for line in open("query.ohsu.1-63", "r"):
  if line.startswith("<num>"):
    topicid = line.split()[-1].strip()
  if line.startswith("<title>"):
    query = line[7:].strip()
    d[query] = topicid

out = open("queries.txt", "w")

for key in d:
  out.write(key + "\n")

out.close()
