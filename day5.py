import os
import networkx as nx

filename = "day5input.txt"

rules = []
rules2 = []
instructions = []

final_order = []
out_of_order = []
count = 0
count2 = 0

def check_order(current_instruction):
    for index, t in enumerate(current_instruction):
        hardlines = []
        for x in rules:
            tx = x.split("|")[0]
            if tx == t:
                temp = x.split("|")[1].strip()
                hardlines.append(int(temp))
        for prev_index in range(index):
            if int(current_instruction[prev_index]) in hardlines:
                out_of_order.append(current_instruction)
                return False
    return True   

with open(filename, "r") as f:
    lines = f.readlines()
    for x in lines:
        if len(x) == 6:
            ts = x.strip()
            rules2.append((ts.split("|")[0], ts.split("|")[1]))
            rules.append(x.strip())
        else:
            instructions.append(x.strip())

first_num_rules = []

for x in rules:
    first_num_rules.append(x.split("|")[0])

set1 = set()
for x in first_num_rules:
    set1.add(x)

for x in instructions:
    if x != '':
        current_instruction = x.split(",")
        if check_order(current_instruction):
            final_order.append(current_instruction)
            midpt = len(current_instruction) // 2
            midnum = int(current_instruction[midpt])
            count += midnum

def jonPlan(current):
    global count2
    G = nx.DiGraph()

    for rule in rules2:
        G.add_edge(rule[0], rule[1])
    
    subgraph = G.subgraph(current)
    if nx.is_directed_acyclic_graph(subgraph):
        sorted_items = list(nx.topological_sort(subgraph))


    
    

    
    midpt = len(sorted_items) // 2
    midnum = int(sorted_items[midpt])
    count2 += midnum

print(f"Part 1 middle nums added = {count}")

for x in out_of_order:
    jonPlan(x)

      
print(f"Part 2 middle nums added = {count2}")   