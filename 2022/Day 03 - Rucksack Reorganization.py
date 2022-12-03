rucksack = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()
rucksack = open("inputs/day03.txt").read().splitlines()

score = 0
for line in rucksack:
    unique = (set(line[:len(line) // 2]) & set(line[len(line) // 2:])).pop()
    if unique.islower():
        score += ord(unique) - ord('a') + 1
    else:
        score += ord(unique) - ord('A') + 27
print("answer 1:", score)

score = 0
for i in range(0, len(rucksack), 3):
    unique = (set(rucksack[i]) & set(rucksack[i + 1]) & set(rucksack[i + 2])).pop()
    if unique.islower():
        score += ord(unique) - ord('a') + 1
    else:
        score += ord(unique) - ord('A') + 27
print("answer 2:", score)
