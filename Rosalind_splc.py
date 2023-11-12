#RNA splicing
import re
uneditedrna = ''
editedrna = ''
introns = []
cut_rna = []
amino_sequence = ''
sequences = {}
file = open ("rosalind_splc.txt")

coding_table = {
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT':'S', 'AGC':'S', 
    'TTT': 'F', 'TTC': 'F',
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'TAT': 'Y', 'TAC': 'Y',
    'TGT': 'C', 'TGC': 'C',
    'TGG': 'W', 
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    'ATG': 'M', 
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
    'AAT': 'N', 'AAC': 'N', 
    'AAA': 'K', 'AAG': 'K',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'TAA': 'end', 'TAG': 'end', 'TGA': 'end'
}


for line in file:
    if line.startswith('>'):
        name = line[1:].rstrip('\n')
        sequences[name] = ''
    else:
        sequences[name] = sequences[name] +line.rstrip('\n')

for item in sequences.keys ():
    introns.append (sequences[item])

uneditedrna = str(introns[0])
introns.pop(0)

for intron in introns:
    if intron == introns[0]:
        editedrna = uneditedrna.replace (intron,'')
        test = len(editedrna)
    else:
        editedrna = editedrna.replace (intron,'')
        test = (len(editedrna))


for i in range(0, len(editedrna), 3):    
    cut_rna.append(editedrna[i:i+3]) 
for element in cut_rna:
    amino_sequence += coding_table [str(element)]

print (amino_sequence)
