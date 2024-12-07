from itertools import product

filename = "day7input.txt"

equations = []
eq_sum = 0

def evaluate_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = int(tokens[i + 1])
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '^':
            #write the two numbers as 1 number so 12 and 33 would be 1233
            result = int(str(result) + str(num))
        i += 2
    return result

def part1(target, nums):
    operations = ['+', '*', '^']
    for ops in product(operations, repeat=len(nums)-1):
        expression = " ".join(f"{nums[i]} {ops[i]}" for i in range(len(nums)-1)) + f" {nums[-1]}"
        if evaluate_left_to_right(expression) == target:
            print(target, expression)
            return True
    return False

with open(filename, "r") as f:
    lines = f.readlines()
    for x in lines:
        equations.append(x.strip())

for x in equations:
    target = x.split(":")[0] 
    nums = x.split(":")[1].split(" ")
    nums = [x for x in nums if x != ""]
    if part1(int(target), nums):
        eq_sum += int(target)


print(eq_sum)