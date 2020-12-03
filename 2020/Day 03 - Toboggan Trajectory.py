geology = []
for slope in open("inputs/day03.txt"):
    geology.append([*slope.strip()])


def tree_count(x_length, y_length):
    trees = 0
    x, y = 0, 0
    while y < (len(geology) - y_length):
        x, y = x + x_length, y + y_length
        if geology[y][x % len(geology[y])] == "#":
            trees += 1
    return trees


print("answer 1:", tree_count(3, 1))
print("answer 2:", tree_count(1, 1) * tree_count(3, 1) * tree_count(5, 1) * tree_count(7, 1) * tree_count(1, 2))
