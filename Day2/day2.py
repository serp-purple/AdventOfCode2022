with open('inputday2.txt', 'r') as f:
    FileContent = f.read()

NewContent = [x.replace(" ","") for x in FileContent.split("\n")]
TotalScore = 0

#score gained by the choice of hand sign
for x in NewContent:
    if(x[1]=="X"): TotalScore +=1
    elif(x[1]=="Y"): TotalScore +=2
    else: TotalScore +=3

#score gained by winning
for x in NewContent:
    if((x[1]=="X" and x[0]=="A")or(x[1]=="Y" and x[0]=="B")or(x[1]=="Z" and x[0]=="C")): TotalScore +=3 #draw
    elif((x[1]=="X" and x[0]=="B")or(x[1]=="Y" and x[0]=="C")or(x[1]=="Z" and x[0]=="A")): continue #lose
    else: TotalScore+=6 #win

print(TotalScore) #answer for part 1



#part 2
TotalScore = 0

for x in NewContent:
    #lose
    if(x[1]=="X"):
        if(x[0]=="A"): TotalScore+=3
        elif(x[0]=="B"): TotalScore+=1
        else: TotalScore+=2
    #draw
    elif(x[1]=="Y"):
        TotalScore+=3
        if(x[0]=="A"): TotalScore+=1
        elif(x[0]=="B"): TotalScore+=2
        else: TotalScore+=3
    #win
    else:
        TotalScore+=6
        if(x[0]=="A"): TotalScore+=2
        elif(x[0]=="B"): TotalScore+=3
        else: TotalScore+=1

print(TotalScore) #part 2 answer