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

def getTreeView(trees: list[list[int]], row: int, col: int, row_dir: int, col_dir: int) -> int:
    prev_row = -1
    prev_col = -1
    viewDistance = -1
    while row >= 0 and row < len(trees) and col >= 0 and col < len(trees[0]):
        viewDistance += 1

        if prev_row == -1 or prev_col == -1:
            prev_row = row
            prev_col = col
        elif trees[row][col] >= trees[prev_row][prev_col]:
            break
        
        row += row_dir
        col += col_dir

    return viewDistance 


def getScenicScore(trees: list[list[int]], row: int, col: int) -> int:
    up = -1
    down = 1
    stationary = 0
    left = -1
    right = 1

    leftScore = getTreeView(trees, row, col, stationary, left)
    rightScore = getTreeView(trees, row, col, stationary, right)
    upScore = getTreeView(trees, row, col, up, stationary)
    downScore = getTreeView(trees, row, col, down, stationary)

    return leftScore * rightScore * upScore * downScore

answer = 0
for row in range(len(trees)):
    for col in range(len(trees[0])):
        answer = max(answer, getScenicScore(trees, row, col))

print(answer)