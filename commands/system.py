
import sys
from tree import Tree

DIRFILE = sys.argv[1]
TRAINTREE = sys.argv[2]
TESTTXT = sys.argv[3]
TESTTREE = sys.argv[4]
M = int(sys.argv[5])
N = int(sys.argv[6])
print M,N

with open(DIRFILE, "r") as f:
	with open(TESTTXT, "w") as fw:
		with open(TESTTREE, "w") as fwt:
			l = f.readlines()
			for line in l[-N:]:
				fwt.write(line)
				t = Tree.parse(line.strip())
				fw.write(t.tosent()+'\n')
				
with open(DIRFILE, "r") as f:
	with open(TRAINTREE, "w") as ftrain:
		l = f.readlines()
		for line in l[:M]:
			ftrain.write(line)