from collections import Counter
from itertools import groupby

output_jolts = sorted(list(map(int, open("inputs/day10.txt"))))
output_jolts.insert(0, 0)
output_jolts.append(max(output_jolts) + 3)
diffs = []
for i in range(len(output_jolts) - 1):
    diffs.append(output_jolts[i + 1] - output_jolts[i])
print("answer 1:", Counter(diffs)[1] * Counter(diffs)[3])


def fib3(term):
    if term <= 2:
        return max(1, term)
    else:
        return fib3(term - 1) + fib3(term - 2) + fib3(term - 3)


count = 1
for key, values in groupby(diffs):
    if key == 1:
        count *= fib3(len(list(values)))
print("answer 2:", count)
