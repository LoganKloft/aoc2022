from abc import ABC, abstractmethod
import os

class Crate():
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

class Stack():
    def __init__(self) -> None:
        self.crates: list[Crate] = []

    def pop(self) -> Crate:
        return self.crates.pop()

    def preappend(self, crate: Crate) -> None:
        self.crates.insert(0, crate)
    
    def append(self, crate: Crate) -> None:
        self.crates.append(crate)
    
    def empty(self) -> bool:
        return not bool(self.crates)
    
    def top(self) -> Crate:
        return self.crates[-1]


class Command(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def do(self) -> None:
        pass

class MoveCommand(Command):
    def __init__(self, leftStack: Stack, rightStack: Stack, numCrates: int) -> None:
        self.leftStack: Stack = leftStack
        self.rightStack: Stack = rightStack
        self.numCrates: int = numCrates
    
    def do(self) -> None:
        cratesToMove: list[Crate] = []
        for _ in range(self.numCrates):
            cratesToMove.append(self.leftStack.pop())
        
        while cratesToMove:
            self.rightStack.append(cratesToMove.pop())

stacks: list[Stack] = []
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as puzzleInput:
    for puzzleLine in puzzleInput:

        if puzzleLine.startswith("move"):
            moveLine = puzzleLine.split()
            MoveCommand(stacks[int(moveLine[3]) - 1], stacks[int(moveLine[5]) - 1], int(moveLine[1])).do()
        
        if "[" in puzzleLine:
            symbolIdx = 1
            while symbolIdx < len(puzzleLine):
                stackIdx = symbolIdx // 4
                if len(stacks) <= stackIdx:
                    stacks.append(Stack())

                if puzzleLine[symbolIdx] == " ":
                    symbolIdx += 4
                    continue
                
                stacks[stackIdx].preappend(Crate(puzzleLine[symbolIdx]))
                symbolIdx += 4

answer = ""
for stack in stacks:
    if not stack.empty():
        answer += stack.top().symbol

print(f"Day 5 Puzzle 2: {answer}")