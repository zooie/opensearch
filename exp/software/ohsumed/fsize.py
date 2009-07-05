
# total size in bytes of a dir
# used for measuring index sizes

import os
import sys

size = 0
for f in os.listdir(sys.argv[1]):
  size += os.path.getsize(sys.argv[1].rstrip("/") + "/" + f)
print "Size", size
