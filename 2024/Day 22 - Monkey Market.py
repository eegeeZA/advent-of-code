import collections

try:
    codes = open("inputs/day22.txt").read()
except FileNotFoundError:
    codes = """
1
2
3
2024
"""[1:]
codes = list(map(int, codes.splitlines()))

deltas = [[] for _ in range(len(codes))]
prices = [{} for _ in range(len(codes))]
for _ in range(2000):
    for i in range(len(codes)):
        secret = codes[i]
        result = secret * 64
        secret ^= result
        secret %= 16777216
        result = secret // 32
        secret ^= result
        secret %= 16777216
        result = secret * 2048
        secret ^= result
        secret %= 16777216

        deltas[i].append(secret % 10 - codes[i] % 10)
        if len(deltas[i]) > 4 and tuple(deltas[i][-4:]) not in prices[i]:
            prices[i][tuple(deltas[i][-4:])] = secret % 10

        codes[i] = secret
print("answer 1:", sum(codes))

best = collections.Counter()
for price in prices:
    best.update(price)
print("answer 2:", best.most_common(1)[0][1])
