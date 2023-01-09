import collections

positions = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""[1:].splitlines()
positions = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""[1:].splitlines()
positions = open("inputs/day09.txt").read().splitlines()

visited1 = collections.defaultdict(int)
visited9 = collections.defaultdict(int)
knots = [(0, 0)] * 10
for position in positions:
    direction, distance = position.split()
    for step in range(int(distance)):
        x, y = knots[0]
        if direction == "R":
            y += 1
        elif direction == "L":
            y -= 1
        elif direction == "U":
            x += 1
        elif direction == "D":
            x -= 1
        knots[0] = x, y

        for i in range(len(knots) - 1):
            x, y = knots[i]
            a, b = knots[i + 1]
            if abs(y - b) > 1 or abs(x - a) > 1:
                if x != a:
                    a += 1 if x > a else -1
                if y != b:
                    b += 1 if y > b else -1
            knots[i + 1] = a, b

        visited1[knots[1]] = True
        visited9[knots[9]] = True

print("answer 1:", sum(visited1.values()))
print("answer 2:", sum(visited9.values()))
