import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

filename = "day6input.txt"
tiles_walked = []
direction = (-1,0)
intersection = []
guard_pos = (0, 0)
start_direction = (-1, 0)
debug_iter = 0


def load_grid(filename):
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f]
        grid_array = np.array(grid, dtype=str)
        return grid_array

grid = load_grid(filename)

def found_guard(row, col):
    global grid
    move_guard(row, col)

def move_guard(starting_row, starting_col):
    global direction
    global tiles_walked
    global grid
    next_step = (starting_row + direction[0], starting_col + direction[1])
    if check_bounds(next_step[0], next_step[1]):
        if grid[next_step[0], next_step[1]] != "#":
            for x in tiles_walked:
                if x == (next_step[0], next_step[1]):
                    intersection.append((next_step[0], next_step[1], direction))
            tiles_walked.append((next_step[0], next_step[1]))

            return next_step[0], next_step[1]
        elif grid[next_step[0], next_step[1]] == "#":
            if direction == (1, 0):
                direction = (0, -1)
            elif direction == (0, 1):
                direction = (1, 0)
            elif direction == (-1, 0):
                direction = (0, 1)
            elif direction == (0, -1):
                direction = (-1, 0)
            return starting_row, starting_col
    else:
        return -1, -1

def check_bounds(row, col):
    global grid
    if row >= 0 and row <= 129 and col >= 0 and col <= 129:
        return True
    
    return False

def part_2():
    global tiles_walked
    global grid
    global guard_pos
    global start_direction
    global debug_iter
    loops = 0
    original_guard_pos = guard_pos
    original_start_direction = start_direction
    set23 = set(tiles_walked)
    for x in set23:
        gridCopy = grid.copy()
        gridCopy[x[0], x[1]] = "#"
        guard_pos = original_guard_pos  # Reset guard position
        start_direction = original_start_direction  # Reset start direction
        if move_guard2(gridCopy):
            loops += 1
    print(f"Part 2: {loops}")

def move_guard2(grid_copy):
    global direction
    global guard_pos
    global start_direction
    global debug_iter
    new_direction = start_direction
    iters = 0
    starting_pos = guard_pos
    while True:
        
        if iters > 139*139:
            print(grid_copy)
            print("Infinite loop detected")
            return True
        
        next_step = (starting_pos[0] + new_direction[0], starting_pos[1] + new_direction[1])
        
        if check_bounds(next_step[0], next_step[1]):
            if grid_copy[next_step[0], next_step[1]] != "#":
                starting_pos = next_step
                iters += 1
            else:
                # Rotate to the right
                if new_direction == (1, 0):
                    new_direction = (0, -1)
                elif new_direction == (0, 1):
                    new_direction = (1, 0)
                elif new_direction == (-1, 0):
                    new_direction = (0, 1)
                elif new_direction == (0, -1):
                    new_direction = (-1, 0)
        else:
            break
    return False
        
new_pos = (0, 0)
for x in range(0, len(grid)):
    for y in range(0, len(grid[x])):
        if grid[x][y] == "^":
            print(f"Found guard at {x}, {y}")
            guard_pos = (x, y)
            new_pos = (x, y)
            break
while True:
    new_pos = move_guard(new_pos[0], new_pos[1])
    if new_pos == (-1, -1):
        break


set1 = set(tiles_walked)
print(f"Total tiles walked: {len(set1)}")
part_2()
