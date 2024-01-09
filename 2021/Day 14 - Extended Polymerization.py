import functools
import itertools
from collections import Counter

try:
    instructions = open("inputs/day14.txt").read()
except FileNotFoundError:
    instructions = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

polymer_template, rules_raw = instructions.split("\n\n")
insertion_rules = {}
for rule in rules_raw.splitlines():
    adjacent, insertion = rule.split(" -> ")
    insertion_rules[tuple(adjacent)] = insertion

mutate_template = polymer_template
for i in range(10):
    new_template = [mutate_template[0]]
    for x, y in itertools.pairwise(mutate_template):
        new_template += [insertion_rules[x, y], y]
    mutate_template = new_template
element_count = list(count for _, count in Counter(mutate_template).most_common())
print("answer 1:", element_count[0] - element_count[-1])


@functools.cache
def count_elements(steps, pair):
    a, b = pair
    result = insertion_rules[pair]
    if steps == 1:
        return Counter([a, result, b])

    return count_elements(steps - 1, (a, result)) - Counter(result) + count_elements(steps - 1, (result, b))


totals = Counter(polymer_template[0])
for x, y in itertools.pairwise(polymer_template):
    totals += count_elements(40, (x, y)) - Counter(x)
element_count = list(count for _, count in totals.most_common())
print("answer 2:", element_count[0] - element_count[-1])
