#finding the genome superstring

file = open('rosalind_long.txt', 'r')
data = {}
datas = []
names = []

for line in file:
    if line.startswith('>'):
        name = line[1:].rstrip('\n')
        data[name] = ''
    else:
        data[name] = data[name] + line.rstrip('\n')

# stores the keys
for item in data.keys():
    names.append(item)

# stores the sequences
for key in names:
    datas.append(str(data[key]))


def find_continuous_overlap(strings, threshold):
    result = str(strings[0])

    for i in range(1, len(strings)):
        current_string = str(strings[i])
            # Check for overlap at the beginning
        overlap_len = round(min(len(result), (min(len(current_string),len(result))) * threshold))
        for maxoverlap in range(overlap_len, len(current_string)):              
            if current_string.endswith(result[0:maxoverlap]):
                result  = current_string + result[maxoverlap:]  
                break
                # Check for overlap at the end
            elif result.endswith(current_string[0:maxoverlap]):
                result = result + current_string[maxoverlap:]
                break
            

    return result


answer = find_continuous_overlap(datas, 0.4)
print(answer)

if answer == datas[0]:
    print(False)
    print(len(answer))
else:
    print(True)
    print(len(answer),len(datas[0]))