import numpy as np
import math
from collections import defaultdict

filename = "day8input.txt"

grid = np.array([list(x.strip()) for x in open(filename, "r")])

anntennas_found = defaultdict(list)
mappings = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

class Node:
    def __init__(self, freq, row, col):
        self.freq = freq
        self.row = row
        self.col = col


def check_bounds(row, col):
    if row >= 0 and row <= 11 and col >= 0 and col <= 11:
        return True
    print("Out of bounds")
    return False

def part_1(grid):
    global anntennas_found
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row, col] != ".":
                print(grid[row, col])
                anntennas_found[grid[row, col]].append(Node(grid[row, col], row, col))
    antinodes = set()
    for freq in anntennas_found:
        for node in anntennas_found[freq]:

            for node2 in anntennas_found[freq]:

                if node == node2:
                    print("sameies")
                    continue
                dx = node2.col - node.col
                dy = node2.row - node.row
                destrow = node.row - dy
                destcol = node.col - dx
                if check_bounds(destrow, destcol):
                    antinodes.add((destrow, destcol))
                else:
                    print("Out of bounds")
    print(len(antinodes))

def part_2(grid):
    global anntennas_found
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row, col] != ".":
                print(grid[row, col])
                anntennas_found[grid[row, col]].append(Node(grid[row, col], row, col))
    antinodes = set()
    for freq in anntennas_found:
        for node in anntennas_found[freq]:

            for node2 in anntennas_found[freq]:

                if node == node2:
                    print("sameies")
                    continue
                dx = node2.col - node.col
                dy = node2.row - node.row
                onboard = True
                totaldx = dx
                totaldy = dy
                while onboard:
                    print("In while")
                    destrow = node.row - totaldy
                    destcol = node.col - totaldx
                    if 0<=destrow<len(grid) and 0<=destcol<len(grid[0]):
                        antinodes.add((destrow, destcol))
                        totaldx += dx
                        totaldy += dy
                    else:
                        print("Out of While")
                        onboard = False
                antinodes.add((node.row, node.col))
    print(len(antinodes))

#part_1(grid)        
part_2(grid)