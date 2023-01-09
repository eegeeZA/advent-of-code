import copy
import math
import types

notes = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""[1:].split("\n\n")
notes = open("inputs/day11.txt").read().split("\n\n")

monkeys = []
for note in notes:
    index, items, operation, test, if_true, if_false = note.splitlines()
    monkey = types.SimpleNamespace()
    monkey.items = list(map(int, items[18:].split(", ")))
    monkey.operation = lambda old, op=operation[22:]: eval(str(old) + op)
    monkey.test = lambda x, div=test[21:]: x % int(div) == 0
    monkey.divisible = int(test[21:])
    monkey.if_true = int(if_true[29:])
    monkey.if_false = int(if_false[30:])
    monkey.inspected = 0
    monkeys.append(monkey)
monkeys2 = copy.deepcopy(monkeys)

for _ in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspected += 1
            worry = monkey.operation(item) // 3
            if monkey.test(worry):
                monkeys[monkey.if_true].items.append(worry)
            else:
                monkeys[monkey.if_false].items.append(worry)
        monkey.items = []

active1, active2 = sorted(monkeys, key=lambda x: x.inspected)[-2:]
print("answer 1:", active1.inspected * active2.inspected)

divisible = math.prod(map(lambda x: x.divisible, monkeys2))
for _ in range(10000):
    for monkey in monkeys2:
        for item in monkey.items:
            monkey.inspected += 1
            worry = monkey.operation(item) % divisible
            if monkey.test(worry):
                monkeys2[monkey.if_true].items.append(worry)
            else:
                monkeys2[monkey.if_false].items.append(worry)
        monkey.items = []

active1, active2 = sorted(monkeys2, key=lambda x: x.inspected)[-2:]
print("answer 2:", active1.inspected * active2.inspected)
