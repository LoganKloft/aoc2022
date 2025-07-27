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
    for rucksack in puzzleInput:
        firstCompartment = set([char for char in rucksack.strip()[:len(rucksack.strip()) // 2]])
        secondCompartment = set([char for char in rucksack.strip()[len(rucksack.strip()) // 2:]])
        answer += getPointValue(firstCompartment.intersection(secondCompartment).pop())

print(f"Day 3 Puzzle 1: {answer}")