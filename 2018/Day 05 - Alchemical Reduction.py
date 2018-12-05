import functools
import re


def trigger(full_x, y):
    x = full_x[-1:]
    matching_letter = x.lower() == y.lower()
    opposite_case = x.islower() and y.isupper()
    opposite_case |= x.isupper() and y.islower()
    if matching_letter and opposite_case:
        return full_x[:-1]
    else:
        return full_x + y


polymer = open("inputs/day05.txt").readline().rstrip()

final = functools.reduce(trigger, polymer)
best = len(final)
print("answer 1:", best)

for letter in set(polymer.lower()):
    shortened = re.sub(letter, "", polymer, flags=re.IGNORECASE)
    best = min(best, len(functools.reduce(trigger, shortened)))
print("answer 2:", best)
