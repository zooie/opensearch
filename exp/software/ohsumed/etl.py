
# output format: docid\tcontent\n

out = open("ohsumed.flat", "w")

toindex = False
buffer = {}

for line in open("ohsumed.88-91", "r"):

  if toindex:
    buffer[toindex] = line.strip()
    toindex = False
    continue

  if line.startswith(".") and not line.startswith(".I") and not line.startswith(".P"):
    if len(buffer) == 6:
      out.write(buffer[".U"] + "\t" + " ".join([buffer[k] for k in buffer if k != ".U"]) + "\n")
      buffer = {}
    toindex = line.strip()

out.close()
