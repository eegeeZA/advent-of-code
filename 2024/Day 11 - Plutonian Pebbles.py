import functools

try:
    stones = open("inputs/day11.txt").read()
except FileNotFoundError:
    stones = """
125 17
"""[1:]
stones = stones.split()

for i in range(25):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            new_stones.append(stone[:len(stone) // 2])
            new_stones.append(str(int(stone[len(stone) // 2:])))
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = new_stones
print("answer 1:", len(stones))


@functools.cache
def find_total(iterations, check_stone):
    if iterations == 0:
        return 1
    if check_stone == '0':
        return find_total(iterations - 1, '1')
    elif len(check_stone) % 2 == 0:
        return (find_total(iterations - 1, check_stone[:len(check_stone) // 2])
                + find_total(iterations - 1, str(int(check_stone[len(check_stone) // 2:]))))
    else:
        return find_total(iterations - 1, str(int(check_stone) * 2024))


total = 0
for stone in open("inputs/day11.txt").read().split():
    total += find_total(75, stone)
print("answer 2:", total)
