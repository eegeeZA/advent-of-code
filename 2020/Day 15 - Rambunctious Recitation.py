memory = [int(x) for x in open("inputs/day15.txt").read().split(",")]
for previous_turn in range(len(memory) - 1, 2020):
    if memory[previous_turn] not in memory[:-1]:
        memory.append(0)
    else:
        indexes = [i for i, x in enumerate(memory) if x == memory[previous_turn]]
        memory.append(int(indexes[-1]) - int(indexes[-2]))
print("answer 1:", memory[-2])

memory = {int(value): [i] for i, value in enumerate(open("inputs/day15.txt").read().split(","))}
last_value = int(open("inputs/day15.txt").read().split(",")[-1])
for i in range(len(memory), 30000000):
    if last_value not in memory or (len(memory[last_value]) < 2):
        last_value = 0
    else:
        last_value = memory[last_value][-1] - memory[last_value][-2]
    if last_value not in memory:
        memory[last_value] = []
    memory[last_value].append(i)
print("answer 2:", last_value)
