import re

pattern = "mul\(\d{1,3},\d{1,3}\)"
pattern3 = "\d{1,3}"
pattern4 = "do\(\)"
pattern5 = "don't\(\)"

sum = 0
sum2 = 0
matches = []
matches2 = []

with open("day3input.txt", "r") as f:
    pzinput = f.read()
    matches = re.findall(pattern, pzinput)
    

bool = True

while bool:
    try:
        dos = True
        dons = False
        if dos:
            betterInput = re.search(pattern5, pzinput)
            
            text = pzinput[:betterInput.start()]
            
            matches2.append(re.findall(pattern, text))
            pzinput = pzinput[betterInput.end():]
            dos = False
            dons = True
        if dons:
            betterInput = re.search(pattern4, pzinput)
            
            pzinput = pzinput[betterInput.end():]
            
            dons = False
            dos = True
    except Exception as e:
        bool = False
        print(e)

for x in matches:
    nums = re.findall(pattern3, x)
    sum += int(nums[0]) * int(nums[1])

for x in matches2:

    for y in x:

        nums2 = re.findall(pattern3, y)
        sum2 += int(nums2[0]) * int(nums2[1])

print("answer 1 : " + str(sum))
print("answer 2 : " + str(sum2))