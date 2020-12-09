from itertools import combinations

all_numbers = list(map(int, open("inputs/day09.txt")))
preamble = 25
weakness = None
for i in range(len(all_numbers) - preamble):
    for x, y in combinations(all_numbers[i:i + preamble], 2):
        if x + y == all_numbers[i + preamble]:
            break
    else:
        weakness = all_numbers[i + preamble]
        break

print("answer 1:", weakness)

for i in range(len(all_numbers)):
    for j in range(i + 2, len(all_numbers)):
        if sum(all_numbers[i:j]) == weakness:
            print("answer 2:", min(all_numbers[i:j]) + max(all_numbers[i:j]))
        elif sum(all_numbers[i:j]) > weakness:
            break
