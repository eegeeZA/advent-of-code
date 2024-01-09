import math

try:
    trees = open("inputs/day08.txt").read().splitlines()
except FileNotFoundError:
    trees = """
30373
25512
65332
33549
35390
"""[1:].splitlines()

trees = [[int(tree) for tree in row] for row in trees]

inner_visible = 0
best_scenic = 0
for i in range(1, len(trees) - 1):
    for j in range(1, len(trees) - 1):
        visible = False
        scenic_scores = []

        scenic = 0
        for check in reversed(range(i)):
            scenic += 1
            if trees[i][j] <= trees[check][j]:
                break
        else:
            visible = True
        scenic_scores.append(scenic)

        scenic = 0
        for check in range(i + 1, len(trees)):
            scenic += 1
            if trees[i][j] <= trees[check][j]:
                break
        else:
            visible = True
        scenic_scores.append(scenic)

        scenic = 0
        for check in reversed(range(j)):
            scenic += 1
            if trees[i][j] <= trees[i][check]:
                break
        else:
            visible = True
        scenic_scores.append(scenic)

        scenic = 0
        for check in range(j + 1, len(trees)):
            scenic += 1
            if trees[i][j] <= trees[i][check]:
                break
        else:
            visible = True
        scenic_scores.append(scenic)

        inner_visible += visible
        best_scenic = max(best_scenic, math.prod(scenic_scores))

print("answer 1:", (len(trees) * 4 - 4) + inner_visible)
print("answer 2:", best_scenic)
