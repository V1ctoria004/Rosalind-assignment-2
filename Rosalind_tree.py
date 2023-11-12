#rosalind tree diagram 


file = open ('rosalind_tree.txt','r')
nodes = int(file.readline())
edges = 0 
edgesfortree = nodes-1 #because trees have n-1 edges
difference = 0

for lines in file:
    edges +=1
#delete one to account for the first line containing the nodes

difference = edgesfortree - edges

print(difference)



