try:
    platform = open("inputs/day14.txt").read().splitlines()
except FileNotFoundError:
    platform = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""[1:].splitlines()

load = 0
for row in zip(*platform):
    for i, space in enumerate("#".join(["".join(sorted(x, reverse=True)) for x in "".join(row).split("#")])):
        if space == "O":
            load += len(row) - i
print("answer 1:", load)

history = []
for _ in range(1_000_000_000):
    platform = ["".join(x) for x in zip(*platform)]
    platform = ["#".join("".join(sorted(piece, reverse=True)) for piece in "".join(x).split("#")) for x in platform]

    platform = ["".join(x) for x in zip(*platform)]
    platform = ["#".join("".join(sorted(piece, reverse=True)) for piece in "".join(x).split("#")) for x in platform]

    platform = ["".join(x) for x in zip(*platform[::-1])]
    platform = ["#".join("".join(sorted(piece, reverse=True)) for piece in "".join(x).split("#")) for x in platform]

    platform = ["".join(x) for x in list(zip(*platform[::-1]))[::-1]]
    platform = ["#".join("".join(sorted(piece, reverse=True)) for piece in "".join(x).split("#")) for x in platform]

    platform = [x[::-1] for x in platform]

    if platform in history:
        break
    history.append(platform)

offset = history.index(platform)
load = 0
for i, part in enumerate(history[offset - 1 + ((1_000_000_000 - offset) % (len(history) - offset))]):
    for space in part:
        if space == "O":
            load += len(part) - i
print("answer 2:", load)
