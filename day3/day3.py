import string
letters = string.ascii_letters
with open ("inputday3.txt", 'r') as file:
    filecontents = [line.strip() for line in file]
    
#lists of contents in both compartments
firstcompartment = [x[:int((len(x)/2))] for x in filecontents]
secondcompartment = [x[int((len(x)/2)):] for x in filecontents]

#a list of repeated items
repeateditems = []
a=0
list1=[]

for x in firstcompartment:
    for z in x:
        if z in secondcompartment[a]:
            if z in list1:
                continue
            else:
                repeateditems.append(z)
                list1.append(z)
    list1.clear()
    a+=1
        
#calculating the sum of the priorities
score =0
for x in repeateditems:
    score += (letters.find(x)+1)
print(score)


#part 2
score = 0
groups = [filecontents[i:i + 3] for i in range(0, len(filecontents), 3)]

for x in groups:
    for z in letters:
        if z in x[0] and z in x[1] and z in x[2]:
            score+=(letters.find(z)+1)
            break

print(score)