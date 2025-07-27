import os

class CleaningAssignment():
    def __init__(self, cleaningAssignment: str) -> None:
        startingSectionIdString, endingSectionIdString = cleaningAssignment.split("-")
        self.startingSectionId = int(startingSectionIdString)
        self.endingSectionId = int(endingSectionIdString)

class CleaningPair():
    def __init__(self, cleaningPair: str) -> None:
        cleaningAssignmentAString, cleaningAssignmentBString = cleaningPair.strip().split(",")
        self.cleaningAssignmentA = CleaningAssignment(cleaningAssignmentAString)
        self.cleaningAssignmentB = CleaningAssignment(cleaningAssignmentBString)
    
    def hasFullOverlap(self) -> bool:
        if self.cleaningAssignmentA.startingSectionId >= self.cleaningAssignmentB.startingSectionId and self.cleaningAssignmentA.endingSectionId <= self.cleaningAssignmentB.endingSectionId:
            return True
        if self.cleaningAssignmentB.startingSectionId >= self.cleaningAssignmentA.startingSectionId and self.cleaningAssignmentB.endingSectionId <= self.cleaningAssignmentA.endingSectionId:
            return True
        return False
    
    def hasOverlap(self) -> bool:
        if self.cleaningAssignmentA.startingSectionId >= self.cleaningAssignmentB.startingSectionId and self.cleaningAssignmentA.startingSectionId <= self.cleaningAssignmentB.endingSectionId:
            return True
        if self.cleaningAssignmentA.endingSectionId >= self.cleaningAssignmentB.startingSectionId and self.cleaningAssignmentA.endingSectionId <= self.cleaningAssignmentB.endingSectionId:
            return True
        if self.cleaningAssignmentB.startingSectionId >= self.cleaningAssignmentA.startingSectionId and self.cleaningAssignmentB.startingSectionId <= self.cleaningAssignmentA.endingSectionId:
            return True
        if self.cleaningAssignmentB.endingSectionId >= self.cleaningAssignmentA.startingSectionId and self.cleaningAssignmentB.endingSectionId <= self.cleaningAssignmentA.endingSectionId:
            return True
        
        return False

answer = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as puzzleInput:
    for cleaningPairString in puzzleInput:
        cleaningPair = CleaningPair(cleaningPairString)
        if cleaningPair.hasOverlap():
            answer += 1

print(f"Day 4 Puzzle 1: {answer}")