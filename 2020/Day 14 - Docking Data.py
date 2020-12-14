import re

result = {}
mask = ""
for instruction in open("inputs/day14.txt"):
    left, right = instruction.strip().split(" = ")
    if left == "mask":
        mask = right
    else:
        mutate = [""] * 36
        for (i, bit_mask), bit in zip(enumerate(mask), bin(int(right))[2:].zfill(36)):
            if bit_mask == "X":
                mutate[i] = bit
            else:
                mutate[i] = mask[i]
        left = int(re.search(r"\d+", left).group(0))
        result[left] = int("".join(mutate), 2)
print("answer 1:", sum(result.values()))


result = {}
mask = ""
for instruction in open("inputs/day14.txt"):
    left, right = instruction.strip().split(" = ")
    if left == "mask":
        mask = right
    else:
        left = int(re.search(r"\d+", left).group(0))
        mutations = [[""] * 36]
        for (i, bit_mask), bit in zip(enumerate(mask), bin(int(left))[2:].zfill(36)):
            if bit_mask == "0":
                for mutate in mutations:
                    mutate[i] = bit
            elif bit_mask == "1":
                for mutate in mutations:
                    mutate[i] = bit_mask
            elif bit_mask == "X":
                new_mutations = []
                for mutate in mutations:
                    new_mutate = mutate.copy()
                    new_mutate[i] = "0"
                    new_mutations.append(new_mutate)
                    new_mutate = mutate.copy()
                    new_mutate[i] = "1"
                    new_mutations.append(new_mutate)
                mutations = new_mutations
        for mutate in mutations:
            result[int("".join(mutate), 2)] = int(right)
print("answer 2:", sum(result.values()))
