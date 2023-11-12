from Bio import Phylo
import io

f = open('rosalind_nkew.txt', 'r')
pairs = [i.split('\n') for i in f.read().strip().split('\n\n')]

for pair in pairs:
    i, line = pair
    values = line.split()
    x = values[0]
    y = values[1]
    tree = Phylo.read(io.StringIO(i), 'newick')
    print('%s' % round(tree.distance(x, y)), end=' ')