f = open("inputday4.txt",'r')
filecontents=f.read().replace('\n',',').replace('-',',').split(',')
filecontents = [filecontents[x:x+4] for x in range(0,len(filecontents),4)]


assignments1 = []
assignments2 = []

for x in filecontents:
    assignments1.append([z for z in range (int(x[0]),int(x[1])+1)])
for x in filecontents:
    assignments2.append([z for z in range (int(x[2]),int(x[3])+1)])

assignments1 = [','.join([str(z) for z in x])for x in assignments1]
assignments2 = [','.join([str(z) for z in x])for x in assignments2]

assignments_containing_the_other = 0

for x in range(len(assignments1)):
    if assignments1[x].endswith(','+assignments2[x]) or assignments2[x].endswith(','+assignments1[x]):
            assignments_containing_the_other+=1
    elif assignments1[x].startswith(assignments2[x]+',') or assignments2[x].startswith(assignments1[x]+','):
        assignments_containing_the_other+=1
    elif (','+assignments1[x]+',' in assignments2[x]) or (','+assignments2[x]+',' in assignments1[x]):
            assignments_containing_the_other+=1
    else:
        if assignments1[x]==assignments2[x]:
            assignments_containing_the_other+=1

print(assignments_containing_the_other)


#part 2
assignments_containing_the_other = 0
assignments1 = [x.split(',') for x in assignments1]
assignments2 = [x.split(',') for x in assignments2]

for x in range(len(assignments1)):
    for z in assignments1[x]:
        if z in assignments2[x]:
            assignments_containing_the_other+=1
            break

print(assignments_containing_the_other)

f.close()
