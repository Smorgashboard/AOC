#Two lists that we need to sort from smallest to largest, we then need the distance between the smallest in list A and the smallest in list B and sum all those values together

#The lists are not cleanly seperated so lets begin there

listA = []
listB = []
sums = 0

#open file and split each line on whitespaces and grab the 0 element and then the 1 element with stripping out newline chars

with open("/Users/hackintosh/Documents/GitHub/AOC/day1input.txt", "r") as f:
    for line in f:
        listA.append(int(line.split("   ")[0]))
        listB.append(int(line.split("   ")[1].strip()))

listA.sort()
listB.sort()

for i in range(0, len(listB)):
   sums += abs(listA[i] - listB[i])
#solution 1 
print(sums)

#Problem two is to sum the numer of times an item in listA appears in listB
simScore = 0

for i in range(0, len(listA)):
    simScore += listB.count(listA[i]) * listA[i]

print(simScore)