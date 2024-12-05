import collections
import functools

try:
    safety_manual = open("inputs/day05.txt").read()
except FileNotFoundError:
    safety_manual = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""[1:]
safety_manual = safety_manual.split("\n\n")

page_orders, page_production = safety_manual
ordering = collections.defaultdict(list)
for rule in page_orders.splitlines():
    before, after = rule.split("|")
    ordering[before].append(after)


def correct(check):
    for i in range(len(check)):
        for part in check[i + 1:]:
            if part not in ordering[check[i]]:
                return False
    return True


def ordered(a, b):
    if a in ordering[b]:
        return 1
    else:
        return -1


middle = 0
middle2 = 0
for instruction in page_production.splitlines():
    pages = instruction.split(",")
    if correct(pages):
        middle += int(pages[(len(pages) - 1) // 2])
    else:
        middle2 += int(sorted(pages, key=functools.cmp_to_key(ordered))[(len(pages) - 1) // 2])

print("answer 1:", middle)
print("answer 2:", middle2)
