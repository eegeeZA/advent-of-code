try:
    rotations = open("inputs/day01.txt").read()
except FileNotFoundError:
    rotations = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""[1:]
rotations = rotations.splitlines()

dial = 50
password = 0
password2 = 0
for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])

    if direction == "L":
        password2 += (dial - 1) // 100 - (dial - distance - 1) // 100
        dial -= distance
    elif direction == "R":
        password2 += (dial + distance) // 100 - dial // 100
        dial += distance

    dial %= 100
    if dial == 0:
        password += 1

print("answer 1:", password)
print("answer 2:", password2)
