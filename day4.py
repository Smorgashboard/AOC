import os
import numpy as np

filename = "day4input.txt"
word = "XMAS"

times_found = 0

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
    new_col = row + d[1]
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
