'''
Reads a tree bank of binary parse trees and finds a 
list of all productions along with their probabilities
Author: Ali Ahmed
'''


from __future__ import division
from tree import Tree
from collections import defaultdict
import sys

TRAINFILE = sys.argv[1]
PRODFILE = sys.argv[2]

freqs = defaultdict(int)
condCounts = defaultdict(int)


with open(TRAINFILE, "r") as f:

    for line in f.readlines():
        line = line.strip()

        t = Tree.parse(line,trunc=True)
        #t.binarize()

        #print t.getProductions()
        prods = t.getProductions()

        for (x,y) in prods:
            freqs[(x,y)] += 1
            condCounts[x] += 1

with open(PRODFILE, "w") as fw:
    for (x,y), freq in freqs.iteritems():
        p = freq / condCounts[x]
        fw.write("%s -> %s # %.4f\n" % (x,y,p))
