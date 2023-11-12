'''
plan:
1. turn fasta into list <3
2. find correct sequences and add them as a node 
    - sequences that appear at least once more in the list 
3. find correct sequences that have compliments and add as a node 
4. find wrong sequences (just check) and add as node 
    - have to remember the wrong nodes in list (?)
5. add a directional edge from the wrong node to its fraternal twin neighbor node 
6. print the directional nodes 

notes: 
- i would have all the steps be one function that then calls upon other functions 


we can ducking do this 
'''
import networkx as nx
G = nx.DiGraph()
file = open('rosalind_corr.txt', 'r')
seqwkey = {}
sequences = []
names = []

for line in file:
    if line.startswith('>'):
        name = line[1:].rstrip('\n')
        seqwkey[name] = ''
    else:
        seqwkey[name] = seqwkey[name] + line.rstrip('\n')

# stores the keys
for item in seqwkey.keys():
    names.append(item)

# stores the sequences
for key in names:
    sequences.append(str(seqwkey[key]))

''''----------'''

def correct(s1, s2):
    return s1 if s1 == s2 else None

def correctrev(s1, s2):
    basesdict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reverse = ''.join(basesdict[base] for base in reversed(s1))
    return s1 if reverse == s2 else None

def correctgathering(information):
    corrected_sequence = set()

    for i in range(len(information)):
        for j in range(len(information)):
            if i != j:
                s1, s2 = information[i], information[j]
                corrected_seq = correct(s1, s2) or correctrev(s1, s2)

                if corrected_seq:
                    corrected_sequence.add(corrected_seq)
                    G.add_node(s1)
                    G.add_node(s2)

    return creatingedges(corrected_sequence, information)

def creatingedges(corrected_sequence, information):
    corrections = set()

    for s1 in information:
        for s2 in corrected_sequence:
            if s1 == s2:
                continue

            # Check for sequences with Hamming distance 1
            if hamming(s1, s2) == 1:
                corrections.add(makingedges(s1, s2))  # s1 is the wrong sequence

            # Check for reversed sequences with Hamming distance 1
            rev_s2 = reversedcheck(s1, s2)
            if rev_s2 and hamming(s1, rev_s2) == 1:
                corrections.add(makingedges(s1, rev_s2))

    return corrections

def hamming(s1, s2):
    return sum(x != y for x, y in zip(s1, s2))

def reversedcheck(s1, s2):
    basesdict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reverse = ''.join(basesdict[base] for base in reversed(s2))
    return reverse if hamming(s1, reverse) == 1 else None

def makingedges(s1, s2):
    return f"{s1}->{s2}"

length = len(sequences[0])
pairs = correctgathering(sequences)
for correction in pairs:
    print(correction)
