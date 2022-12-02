f=open("inputday1.txt",'r')
list1 = []
CalloriesCount = []

lines = f.readlines()

for x in lines:
    if x!="\n":
        list1.append(int(x))
    else:
        CalloriesCount.append(sum(list1))
        list1.clear()

print(max(CalloriesCount))