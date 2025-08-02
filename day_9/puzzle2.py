import os

class KnotLocation():
    def __init__(self):
        self.position: tuple[int] = (0, 0)

locations: list[KnotLocation] = []
for i in range(10):
    locations.append(KnotLocation())

tailVisited = set()
tailVisited.add(locations[-1].position)

def moveTail(tail: KnotLocation, head: KnotLocation):
    if abs(head.position[0] - tail.position[0]) <= 1 and abs(head.position[1] - tail.position[1]) <= 1:
        return
    
    if tail.position[0] == head.position[0]:
        tail.position = (tail.position[0], tail.position[1] + (head.position[1] - tail.position[1]) // abs(head.position[1] - tail.position[1]))
    elif tail.position[1] == head.position[1]:
        tail.position = (tail.position[0] + (head.position[0] - tail.position[0]) // abs(head.position[0] - tail.position[0]), tail.position[1])
    else:
        tail.position = (tail.position[0] + (head.position[0] - tail.position[0]) // abs(head.position[0] - tail.position[0]), tail.position[1] + (head.position[1] - tail.position[1]) // abs(head.position[1] - tail.position[1]))

def moveHead(head: KnotLocation, direction: tuple[int]):
    head.position = (head.position[0] + direction[0], head.position[1] + direction[1])

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as puzzleInput:
    for line in puzzleInput:
        line = line.strip()

        directionSymbol, directionMagnitude = line.split(" ")
        direction = (0, 0)
        directionMagnitude = int(directionMagnitude)

        if directionSymbol == "R":
            direction = (1, 0)
        elif directionSymbol == "L":
            direction = (-1, 0)
        elif directionSymbol == "U":
            direction = (0, 1)
        elif directionSymbol == "D":
            direction = (0, -1)
        
        for _ in range(directionMagnitude):
            moveHead(locations[0], direction)

            for i in range(1, len(locations)):
                moveTail(locations[i], locations[i - 1])

            if locations[-1].position not in tailVisited:
                tailVisited.add(locations[-1].position)

print(len(tailVisited))