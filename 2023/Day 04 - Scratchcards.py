scratchcards = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""[1:].splitlines()
scratchcards = open("inputs/day04.txt").read().splitlines()

points = 0
copies = [1] * len(scratchcards)
for i, scratchcard in enumerate(scratchcards):
    winning, have = scratchcard[scratchcard.index(":") + 1:].split("|")
    winning = set(int(x) for x in winning.split())
    have = set(int(x) for x in have.split())
    if len(winning & have):
        points += 2 ** (len(winning & have) - 1)
        for x in range(len(winning & have)):
            copies[i + 1 + x] += copies[i]

print("answer 1:", points)
print("answer 2:", sum(copies))
