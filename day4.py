import os
import numpy as np

filename = "day4input.txt"
word = "XMAS"

times_found = 0
times_found2 = 0

DIRECTIONS = [
    (0, 1),    # Right
    (0, -1),   # Left
    (1, 0),    # Down
    (-1, 0),   # Up
    (1, 1),    # Down-right (diagonal)
    (1, -1),   # Down-left (diagonal)
    (-1, 1),   # Up-right (diagonal)
    (-1, -1)   # Up-left (diagonal)
]

NEW_DIRECTIONS =[
    (1, 1),    
    (1, -1),   
    (-1, 1),   
    (-1, -1)   
]

def load_grid(filename):
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f]
    grid_array = np.array(grid, dtype=str)
    return grid_array

def found_x(row, col):
    global grid
    for d in DIRECTIONS:
        search_row = row + d[0]
        search_col = col + d[1]
        if search_row >= 0 and search_row  <= 139 and search_col <=139 and search_col >= 0:
            if grid[search_row, search_col] == "M":
                found_m(search_row, search_col, d)

def found_m(row, col, d):
    global grid
    new_row = row + d[0]
    new_col = col + d[1]
    if new_row >= 0 and new_row  <= 139 and new_col <=139 and new_col >= 0:
        if grid[new_row, new_col] == "A":
            found_a(new_row, new_col, d)

def found_a(row, col, d):
    global grid
    global times_found
    new_row = row + d[0]
    new_col = col + d[1]
    if new_row >= 0 and new_row  <= 139 and new_col <=139 and new_col >= 0:
        if grid[new_row, new_col] == "S":
            times_found += 1

grid = load_grid(filename)

print(grid.shape)

for row in range(grid.shape[0]):
    for col in range(grid.shape[1]):
        if grid[row, col] == "X":
            found_x(row, col)

print(f"Total XMAS found: {times_found}")


def part_2(row, col):
    global grid
    global times_found2
    for d in NEW_DIRECTIONS:
        bool1 = False
        bool2 = False
        search_row = row + d[0]
        search_col = col + d[1]
        if search_row >= 0 and search_row  <= 139 and search_col <=139 and search_col >= 0:
            if grid[search_row, search_col] == "M":
                new_row = row + (d[0] * -1)
                new_col = col + (d[1] * -1)
                if new_row >= 0 and new_row  <= 139 and new_col <=139 and new_col >= 0:
                    if grid[new_row, new_col] == "S":
                        bool1 = True
                        bool2 = part_2_check_2(row, col, d)
            elif grid[search_row, search_col] == "S":
                new_row = row + (d[0] * -1)
                new_col = col + (d[1] * -1)
                if new_row >= 0 and new_row  <= 139 and new_col <=139 and new_col >= 0:
                    if grid[new_row, new_col] == "M":
                        bool1 = True
                        bool2 = part_2_check_2(row, col, d)
        if bool1 and bool2:
            print(f"Found at {row}, {col} and direction {d} with grid {grid[search_row, search_col]} at {search_row} {search_col} and {grid[new_row, new_col]} at {new_row} {new_col}")
            times_found2 += 1
            break
            
def part_2_check_2(row, col, d):
    global grid
    if d[0] == 1 and d[1] == 1:
        newd = (-1,1)
    elif d[0] == 1 and d[1] == -1:
        newd = (-1,-1)
    elif d[0] == -1 and d[1] == 1:
        newd = (1,1)
    elif d[0] == -1 and d[1] == -1:
        newd = (1,-1)

    search_row = row + newd[0]
    search_col = col + newd[1]
    if search_row >= 0 and search_row  <= 139 and search_col <=139 and search_col >= 0:
        if grid[search_row, search_col] == "M":
            new_row = row + (newd[0] * -1)
            new_col = col + (newd[1] * -1)
            if new_row >= 0 and new_row  <= 139 and new_col <=139 and new_col >= 0:
                if grid[new_row, new_col] == "S":
                    print(f"Found at {row}, {col} and direction {d} with new direction of {newd} with grid {grid[search_row, search_col]} at {search_row} {search_col} and {grid[new_row, new_col]} at {new_row} {new_col}")
                    return True
                
        elif grid[search_row, search_col] == "S":
            new_row = row + (newd[0] * -1)
            new_col = col + (newd[1] * -1)
            if new_row >= 0 and new_row  <= 139 and new_col <=139 and new_col >= 0:
                if grid[new_row, new_col] == "M":
                    print(f"Found at {row}, {col} and direction {d} with new direction of {newd} with grid {grid[search_row, search_col]} at {search_row} {search_col} and {grid[new_row, new_col]} at {new_row} {new_col}")
                    return True
                
    
    return False

for row in range(grid.shape[0]):
    for col in range(grid.shape[1]):
        if grid[row, col] == "A":
            part_2(row, col)

print(times_found2)