
filename = """C:\\vsc\\AOC\\day9test2.text"""
###### day9test2.text should produce 169
#0...1...2......33333
#0...1...233333......
#0...1...233333......
#02..1....33333......
#021......33333......
#021......33333......


disk_space = []

with open(filename, "r") as f:
    lines = f.readlines()
    for x in lines:
        disk_space.append(x.strip())

def check_list(string_list):
    dots = []
    for i in range(len(string_list)):
        if string_list[i] == ".":
            dots.append(i)

    return min(dots)

def check_nums(string_list):
    nums = []
    for i in range(len(string_list)):
        if string_list[i] != ".":
            nums.append(i)
    return max(nums)

def part_1(line):
    multi = 0
    new_line = ""
    file_block = 0
    for index, x in enumerate(line):
        x = int(x)
        if index % 2 == 0:
            for i in range(x):
                new_line += str(file_block)
                
            file_block += 1
        else:
            for i in range(x):
                new_line += "."
    print(new_line)
    new_dict = {}
    for index, x in enumerate(new_line):
        if x == ".":
            new_dict[index] = x

    string_list = list(new_line)

    reversed_list = string_list[::-1]



    for i in range(len(reversed_list)):
        if i != 0: 
            progress = (i / len(reversed_list)) * 100
        else:
            progress = 0
        if i % 1000 == 0:
            print(f"Current progress : Iteration {i} out of {len(reversed_list)} currently at %{progress}.")
        if reversed_list[i] != ".":        

            try:
                
                key = min(new_dict)
                left_most_dot = check_list(string_list)
                right_most_num = check_nums(string_list)
                if left_most_dot > right_most_num:
                    continue
                new_dict.pop(key)

                string_list[key] = reversed_list[i]
             
                j = i + 1
                string_list[-j] = "."
            except Exception as e:

                pass

    xs_to_remove = string_list.count(".")
    for i in range(xs_to_remove):
        string_list.remove(".")
    for i in range(len(string_list)):
        prod = int(string_list[i]) * i
        multi += prod
    

    return multi

for x in disk_space:
    print(part_1(x))