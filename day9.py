
filename = "day9test.txt"
disk_space = []

with open(filename, "r") as f:
    lines = f.readlines()
    for x in lines:
        disk_space.append(x.strip())

def part_1(line):
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

    new_dict = {}
    for index, x in enumerate(new_line):
        if x == ".":
            new_dict[index] = x

    string_list = list(new_line)
    reversed_list = string_list[::-1]
    for ind, x in enumerate(reversed_list):
        if x != ".":        
            try:
                key = min(new_dict)
                new_dict.pop(key)
                string_list[key] = x
                string_list[ind] = "."
            except:
                pass
    final_string = "".join(string_list)
    print(final_string)
        
for x in disk_space:
    part_1(x)