import re

totalDiff = 0
totalSum = 0
listA = []
listB = []

with open("input_01.txt") as file:
    for line in file:
        
        match = re.match(r"([0-9]+)\s+([0-9]+)", line)
        items = match.groups()
        listA.append(int(items[0]))
        listB.append(int(items[1]))
        
listA.sort()
listB.sort()
            
for i in range(len(listA)):
    totalDiff += abs(listA[i] - listB[i])

print(totalDiff)

for i in range(len(listA)):
    for j in range(len(listB)):
        if(listA[i] == listB[j]):
            totalSum += listA[i]
            
print(totalSum)