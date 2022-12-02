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


list1.clear()
print(max(CalloriesCount)) #answer for part 1
list1.append(max(CalloriesCount))
CalloriesCount.remove(max(CalloriesCount))

for i in range(2):
    list1.append(max(CalloriesCount))
    CalloriesCount.remove(max(CalloriesCount))

print(sum(list1)) #answer for part 2