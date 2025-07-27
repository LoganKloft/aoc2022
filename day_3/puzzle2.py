import os

def getPointValue(item: str) -> int:
    if not item:
        return 0
    if len(item) > 1:
        return 0
    if not item.isalpha():
        return 0
    
    offset = 27 - ord('A') if item.isupper() else 1 - ord('a')
    return ord(item) + offset

answer = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as puzzleInput:
    groups: list[set] = []
    for rucksack in puzzleInput:
        groups.append(set(rucksack.strip()))

        if len(groups) == 3:
            answer += getPointValue((groups[0] & groups[1] & groups[2]).pop())
            groups = []

print(f"Day 3 Puzzle 1: {answer}")