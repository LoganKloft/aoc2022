import os

trees: list[list[int]] = []
treesSeen: list[list[bool]] = []
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as puzzleInput:
    for line in puzzleInput:
        line = line.strip()
        treeLine: list[int] = []
        treeLineSeen: list[bool] = []
        for tree in line:
            treeLine.append(int(tree))
            treeLineSeen.append(False)
        trees.append(treeLine)
        treesSeen.append(treeLineSeen)

def traceLine(trees: list[list[int]], treesSeen: list[list[bool]], row: int, col: int, row_dir: int, col_dir: int):
    prev_row = -1
    prev_col = -1
    while row >= 0 and row < len(trees) and col >= 0 and col < len(trees[0]):
        if prev_row == -1 or prev_col == -1:
            treesSeen[row][col] = True
            prev_row = row
            prev_col = col
        elif trees[prev_row][prev_col] < trees[row][col]:
            treesSeen[row][col] = True
            prev_row = row
            prev_col = col

        row += row_dir
        col += col_dir

up = -1
down = 1
stationary = 0
left = -1
right = 1
# trace top edge
for col in range(len(trees[0])):
    traceLine(trees, treesSeen, 0, col, down, stationary)

# trace bottom edge
for col in range(len(trees[0])):
    traceLine(trees, treesSeen, len(trees) - 1, col, up, stationary)

# trace left edge
for row in range(len(trees)):
    traceLine(trees, treesSeen, row, 0, stationary, right)

# trace right edge
for row in range(len(trees)):
    traceLine(trees, treesSeen, row, len(trees[0]) - 1, stationary, left)

answer = 0
for treeLineSeen in treesSeen:
    for treeSeen in treeLineSeen:
        if treeSeen:
            answer += 1

print(answer)