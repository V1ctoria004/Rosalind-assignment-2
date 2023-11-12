#overlap graphs
'''
the last n characters of s have to be the same as the first n characters of t for it to be a directional graph
from s to t 
but s!==t

we then write the names of the different connections as s t 
'''

file = open ('rosalind_grph.txt')
nodes = {}
vertices = []
sequences = []
edges = []
intermediate = []
n = 3

for line in file:
    if line.startswith('>'):
        name = line[1:].rstrip('\n')
        nodes[name] = ''
    else:
        nodes[name] = nodes[name] +line.rstrip('\n')

#stores the keys 
for item in nodes.keys ():
    vertices.append (item)

#stores the sequences
for key in vertices:
    sequences.append (nodes[key])

for element in range(len(vertices)):
    for thing in range (len(vertices)):
        if element != thing:
            s1 = sequences[element]
            s2 = sequences[thing]
            if s1[-n:] == s2[:n]:
                print(vertices[element], vertices[thing])
            

