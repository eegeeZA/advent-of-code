try:
    paper_rolls = open("inputs/day04.txt").read()
except FileNotFoundError:
    paper_rolls = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""[1:]
paper_rolls = paper_rolls.splitlines()

forklift_access = 0
for x in range(len(paper_rolls)):
    for y in range(len(paper_rolls[x])):
        if paper_rolls[x][y] != "@":
            continue

        neighbor_count = 0
        for dx in range(max(0, x - 1), min(len(paper_rolls), x + 2)):
            for dy in range(max(0, y - 1), min(len(paper_rolls[x]), y + 2)):
                if paper_rolls[dx][dy] == "@" and not (x == dx and y == dy):
                    neighbor_count += 1

        if neighbor_count < 4:
            forklift_access += 1
print("answer 1:", forklift_access)

paper_removed = 0
paper_rolls = [list(line) for line in paper_rolls]
done = False
while not done:
    done = True
    for x in range(len(paper_rolls)):
        for y in range(len(paper_rolls[x])):
            if paper_rolls[x][y] != "@":
                continue

            neighbor_count = 0
            for dx in range(max(0, x - 1), min(len(paper_rolls), x + 2)):
                for dy in range(max(0, y - 1), min(len(paper_rolls[x]), y + 2)):
                    if paper_rolls[dx][dy] == "@" and not (x == dx and y == dy):
                        neighbor_count += 1

            if neighbor_count < 4:
                paper_removed += 1
                paper_rolls[x][y] = "."
                done = False
print("answer 2:", paper_removed)
