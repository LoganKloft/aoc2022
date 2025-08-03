import os
from typing import Callable

class Monkey():
    def __init__(self, id: int, items, processor_func, tester_func) -> None:
        self.id: int = id
        self.items: list[int] = items
        self.processor_func: Callable[[int], int] = processor_func
        self.tester_func: Callable[[int], int] = tester_func
        self.num_inspections = 0

    def process(self) -> list[int]:
        global example
        if self.items:
            self.num_inspections += 1
        else:
            return [-1, -1]
        
        new = self.processor_func(self.items.pop(0))
        new = new % 96577 if example else new % 9699690
        return [self.tester_func(new), new]

monkeys: list[Monkey] = []
example = False
monkeys.append(Monkey(0, [66, 79], lambda x: x * 11, lambda x: 6 if x % 7 == 0 else 7))
monkeys.append(Monkey(1, [84, 94, 94, 81, 98, 75], lambda x: x * 17, lambda x: 5 if x % 13 == 0 else 2))
monkeys.append(Monkey(2, [85, 79, 59, 64, 79, 95, 67], lambda x: x + 8, lambda x: 4 if x % 5 == 0 else 5))
monkeys.append(Monkey(3, [70], lambda x: x + 3, lambda x: 6 if x % 19 == 0 else 0))
monkeys.append(Monkey(4, [57, 69, 78, 78], lambda x: x + 4, lambda x: 0 if x % 2 == 0 else 3))
monkeys.append(Monkey(5, [65, 92, 60, 74, 72], lambda x: x + 7, lambda x: 3 if x % 11 == 0 else 4))
monkeys.append(Monkey(6, [77, 91, 91], lambda x: x * x, lambda x: 1 if x % 17 == 0 else 7))
monkeys.append(Monkey(7, [76, 58, 57, 55, 67, 77, 54, 99], lambda x: x + 6, lambda x: 2 if x % 3 == 0 else 1))

# example = True
# monkeys.append(Monkey(0, [79, 98], lambda x: x * 19, lambda x: 2 if x % 23 == 0 else 3))
# monkeys.append(Monkey(1, [54, 65, 75, 74], lambda x: x + 6, lambda x: 2 if x % 19 == 0 else 0))
# monkeys.append(Monkey(2, [79, 60, 97], lambda x: x * x, lambda x: 1 if x % 13 == 0 else 3))
# monkeys.append(Monkey(3, [74], lambda x: x + 3, lambda x: 0 if x % 17 == 0 else 1))

rounds = 10000
for round in range(rounds):
    for monkey in monkeys:
        while True:
            monkeyId, item = monkey.process()
            if monkeyId == -1:
                break
            monkeys[monkeyId].items.append(item)

for monkey in monkeys:
    print(monkey.id, monkey.num_inspections)