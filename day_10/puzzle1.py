import os

cycle: int = 1
register_x: int = 1
cycles_to_check: list[int] = [20 + 40 * x for x in range(6)]
answer = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as puzzleInput:
    for line in puzzleInput:
        line = line.strip()
        if line.startswith("noop"):
            if cycle in cycles_to_check:
                answer += cycle * register_x
            
            cycle += 1
        elif line.startswith("addx"):
            for _ in range(2):
                if cycle in cycles_to_check:
                    answer += cycle * register_x
                cycle += 1
            register_x += int(line.split(" ")[1])

    if cycle in cycles_to_check:
        answer += cycle * register_x

print(answer)