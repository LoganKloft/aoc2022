import os

width = 40
height = 6
crt_radius = 1
cycle: int = 0
register_x: int = 1
drawing = [['.' for _ in range(width)] for _ in range(height)]
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as puzzleInput:
    for line in puzzleInput:
        line = line.strip()
        if line.startswith("noop"):
            if abs(cycle % 40 - register_x) <= crt_radius:
                drawing[cycle // width][cycle % width] = '#'
            cycle += 1
        elif line.startswith("addx"):
            for _ in range(2):
                if abs(cycle % 40 - register_x) <= crt_radius:
                    drawing[cycle // width][cycle % width] = '#'
                cycle += 1
            register_x += int(line.split(" ")[1])

    if abs(cycle % 40 - register_x) <= crt_radius:
        drawing[cycle // width][cycle % width] = '#'
    
for row in drawing:
    for cell in row:
        print(cell, end='')
    print()