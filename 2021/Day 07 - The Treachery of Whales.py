try:
    crabs = list(map(int, open("inputs/day07.txt").read().split(",")))
except FileNotFoundError:
    crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

print("answer 1:", min(sum(abs(crab - i) for crab in crabs) for i in range(max(crabs))))
print("answer 2:", min(sum(abs(crab - i) * (abs(crab - i) + 1) // 2 for crab in crabs) for i in range(max(crabs))))
