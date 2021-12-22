import collections

algorithm_with_image = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""[1:]
algorithm_with_image = open("inputs/day20.txt").read()

algorithm, image = algorithm_with_image.split("\n\n")
image = image.splitlines()
infinite_image = collections.defaultdict(bool, {(i, j): image[i][j] == "#" for i in range(len(image))
                                                for j in range(len(image[i].rstrip()))})


def enhance(input_image, level):
    result = input_image.copy()

    for limit in range(level):
        new_image = result.copy()
        min_range = 0 - (1 + limit)
        max_range = len(image) + (1 + limit)
        for x in range(min_range, max_range):
            for y in range(min_range, max_range):
                binary_string = "".join([str(int(result[i, j]))
                                         for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)])
                new_image[x, y] = algorithm[int(binary_string, 2)] == "#"

        result = new_image

        if algorithm[0] == "#":
            if limit % 2:
                result.default_factory = lambda: algorithm[-1] == "#"
            else:
                result.default_factory = lambda: algorithm[0] == "#"

    return sum(result.values())


print("answer 1:", enhance(infinite_image, 2))
print("answer 2:", enhance(infinite_image, 50))
