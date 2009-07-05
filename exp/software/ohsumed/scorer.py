
# usage: cat results.txt | python scorer [count=10]
# computes DCG @ count (default 10) as relevancy score
# pass in results.txt through stdin (results.txt format: query_text\wdocid\n)

import math

def parse_query_map():
  d = {}
  topicid = None

  for line in open("query.ohsu.1-63", "r"):
    if line.startswith("<num>"):
      topicid = line.split()[-1].strip()
    if line.startswith("<title>"):
      query = line[7:].strip()
      d[query] = topicid

  return d

def parse_relev_map():
  d = {}

  for line in open("qrels.ohsu.88-91", "r"):
    topicid, docid, relev = line.strip().split()
    d[topicid.strip() + docid.strip()] = int(relev)

  return d

def lookup_relev(query, docid, qmap, rmap):
  topicid = qmap[query.strip()]
  key = topicid + docid.strip()
  if key in rmap:
    return rmap[key]
  else:
    return 0

def score():
  qmap = parse_query_map()
  rmap = parse_relev_map()

  import sys

  count = 10
  if len(sys.argv) > 1:
    count = int(sys.argv[1])

  r = {}
  for line in sys.stdin:
    tokens = line.split()
    q = " ".join(tokens[:-1])
    docid = tokens[-1]
    v = lookup_relev(q, docid, qmap, rmap)
    if q in r:
       #old, size = r[q]
       #i = size + 1
       r[q].append(v)
    else:
      #r[q] = (v, 1)
      r[q] = [v]

  total = 0
  for q, vs in r.iteritems():
    for i, v in enumerate(vs[:count]):
      denom = 1
      if i != 0:
        denom = math.log(i + 1, 2)
      total += v / denom
  a_dcg = total / len(r)

  print "Avg. DCG", a_dcg

if __name__ == "__main__":
  score()
