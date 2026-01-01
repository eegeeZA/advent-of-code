try:
    joltage_ratings = open("inputs/day03.txt").read()
except FileNotFoundError:
    joltage_ratings = """
987654321111111
811111111111119
234234234234278
818181911112111
"""[1:]
joltage_ratings = joltage_ratings.splitlines()

joltage = 0
for joltage_rating in joltage_ratings:
    ratings = list(map(int, list(joltage_rating)))
    best = max(ratings[:-1])
    joltage += int(str(best) + str(max(ratings[ratings.index(best) + 1:])))
print("answer 1:", joltage)

joltage = 0
for joltage_rating in joltage_ratings:
    ratings = list(map(int, list(joltage_rating)))
    digits = []
    divider = 0
    for i in range(11, 0, -1):
        best = max(ratings[divider:-i])
        digits.append(str(best))
        divider = ratings.index(best, divider) + 1
    digits.append(str(max(ratings[divider:])))
    joltage += int(''.join(digits))
print("answer 2:", joltage)
