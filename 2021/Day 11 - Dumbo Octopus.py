import itertools

octopuses_raw = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]
octopuses_raw = open("inputs/day11.txt").read().splitlines()

octopuses = [[int(octopus) for octopus in octopus_row] for octopus_row in octopuses_raw]
neighbours = {(i, j): [(x, y) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)
                       if 0 <= x < len(octopuses) and 0 <= y < len(octopuses) and (x != i or y != j)]
              for i in range(len(octopuses)) for j in range(len(octopuses))}


def flash(total=0):
    for i, octopus_row in enumerate(octopuses):
        for j, octopus in enumerate(octopus_row):
            if octopuses[i][j] > 9:
                octopuses[i][j] = 0
                for x, y in neighbours[(i, j)]:
                    if octopuses[x][y] > 0:
                        octopuses[x][y] += 1
                return flash(total + 1)
    return total


flash_100_count = 0
all_flash_step = None
for step in itertools.count():
    for i in range(len(octopuses)):
        for j in range(len(octopuses)):
            octopuses[i][j] += 1
    flash_count = flash()
    if step < 100:
        flash_100_count += flash_count
    if flash_count == len(octopuses) * len(octopuses):
        all_flash_step = step + 1
        break

print("answer 1:", flash_100_count)
print("answer 2:", all_flash_step)
