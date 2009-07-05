
# computes average query length (# of tokens)

total = 0
count = 0
for line in open("queries.txt", "r"):
  total += len(line.split())
  count += 1
print "AVG Query Length", total / float(count)
