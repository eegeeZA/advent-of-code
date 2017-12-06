banks_input = "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5"
banks = list(map(int, banks_input.split()))
seen = []
redistributions = 0
while True:
    configuration = ",".join(map(str, banks))
    if configuration in seen:
        break
    seen.append(configuration)
    max_bank = max(banks)
    i = banks.index(max_bank)
    banks[i] = 0
    for block in range(max_bank):
        i += 1
        banks[i % len(banks)] += 1
    redistributions += 1
print("answer 1:", redistributions)

banks = list(map(int, banks_input.split()))
seen = {}
redistributions = 0
while True:
    configuration = ",".join(map(str, banks))
    if configuration in seen:
        break
    seen[configuration] = redistributions
    max_bank = max(banks)
    i = banks.index(max_bank)
    banks[i] = 0
    for block in range(max_bank):
        i += 1
        banks[i % len(banks)] += 1
    redistributions += 1
print("answer 2:", redistributions - seen[configuration])
