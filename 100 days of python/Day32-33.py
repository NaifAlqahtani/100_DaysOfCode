listA = []
listB = []

for a in range(3,18,2):
    listA.append(a)

for b in range(2,17,2):
    listB.append(b)

for x in listA:
    for y in listB:
        print(x,y)