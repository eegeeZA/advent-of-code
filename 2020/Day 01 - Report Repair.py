from itertools import combinations

expenses = list(map(int, open("inputs/day01.txt")))

for expense in expenses:
    if 2020 - expense in expenses:
        print("answer 1:", expense * (2020 - expense))
        break

for expense1, expense2, expense3 in combinations(expenses, 3):
    if (expense1 + expense2 + expense3) == 2020:
        print("answer 2:", expense1 * expense2 * expense3)
        break
