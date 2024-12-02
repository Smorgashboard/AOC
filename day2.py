import numpy as np

safeReports = 0
checkAgain = []

#Check if absolute value of differnce is between 1 and 3
def isGradual(arr):
    diffs = np.abs(np.diff(arr))
    return np.all((diffs >= 1) & (diffs <= 3))

def doubleCheck(arr, index):
    #we gotta check if removing JUST 1 value fixes the issue

    newArr = np.array(np.delete(arr, index))

    if np.all(np.diff(newArr) <0) or np.all(np.diff(newArr) >0):
        if isGradual(newArr) == True:
            return True

# Read input
reportValues = []
with open("day2input.txt", "r") as f:
    for line in f:
        nums = list(map(int, line.strip().split()))
        reportValues.append(nums)
        
# Evaluate each report
for report in reportValues:
    npArr = np.array(report)
    if np.all(np.diff(npArr) <0) or np.all(np.diff(npArr) >0):
        if isGradual(npArr) == True:
            safeReports += 1
        else:
            checkAgain.append(npArr.copy())
    else:
        booly = False
        for i in range(0, len(npArr)):
            bolo = doubleCheck(npArr.copy(), i)
            if bolo == True:
                booly = True
                safeReports += 1
                break
        if booly == False:
            checkAgain.append(npArr.copy())

for x in checkAgain:
    newNpArr = np.array(x)
    for i in range(0, len(newNpArr)):
        boloy = doubleCheck(newNpArr.copy(), i)
        if boloy == True:
            safeReports += 1
            break
        
print(safeReports)
