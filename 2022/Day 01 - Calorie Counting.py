calories = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
calories = open("inputs/day01.txt").read()

total = []
for x in calories.split("\n\n"):
    sub_total = 0
    for y in x.split("\n"):
        sub_total += int(y)
    total.append(sub_total)

total = sorted(total)

print("answer 1:", total[-1])
print("answer 2:", sum(total[-3:]))
