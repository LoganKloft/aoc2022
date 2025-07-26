import os

class FoodItem():
    def __init__(self, calories: int):
        self.calories = calories

class Elf():
    def __init__(self, id: int) -> None:
        self.foodItems = []
        self.id = id
    
    def addFoodItem(self, foodItem: FoodItem) -> None:
        self.foodItems.append(foodItem)
    
    def getCalorieCount(self) -> int:
        return sum(foodItem.calories for foodItem in self.foodItems)

class ElfCalorieLine():
    def __init__(self, elfCalorieLine: str):
        elfCalorieLine = elfCalorieLine.strip()
        self.calories = 0
        self.containsCalories = False

        if elfCalorieLine:
            self.calories = int(elfCalorieLine)
            self.containsCalories = True

    def __bool__(self) -> True:
        return self.containsCalories

    def getCalories(self) -> int:
        return self.calories

elves = []
elfId = 1
elf = Elf(elfId)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as elfCalorieFile:
    for elfCalorieLine in elfCalorieFile:
        elfCalorieLine = ElfCalorieLine(elfCalorieLine)

        if elfCalorieLine:
            elf.addFoodItem(FoodItem(elfCalorieLine.getCalories()))
        else:
            elves.append(elf)
            elf = Elf(elfId)
            elfId += 1

elves.append(elf)
elf = Elf(elfId)
elfId += 1

answer = max(elf.getCalorieCount() for elf in elves)
print(f"Day 1, Puzzle 1: {answer}")