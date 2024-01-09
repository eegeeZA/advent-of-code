from collections import Counter
from itertools import compress

try:
    diagnostics = open("inputs/day03.txt").read().splitlines()
except FileNotFoundError:
    diagnostics = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
                   "01010"]

gamma_rating = epsilon_rating = ""
for diagnostic in zip(*diagnostics):
    (gamma_rate, _), (epsilon_rate, _) = Counter(diagnostic).most_common()
    gamma_rating += gamma_rate
    epsilon_rating += epsilon_rate
print("answer 1:", int(gamma_rating, 2) * int(epsilon_rating, 2))

oxygen_rating = co2_rating = ""
oxygen_criteria = [True] * len(diagnostics)
co2_criteria = [True] * len(diagnostics)
for diagnostic in zip(*diagnostics):
    try:
        (oxygen_rate, most_common), (_, least_common) = Counter(compress(diagnostic, oxygen_criteria)).most_common()
        if most_common == least_common:
            oxygen_rate = "1"
    except ValueError:
        oxygen_rate = next(compress(diagnostic, oxygen_criteria))
    oxygen_criteria = [x and y for x, y in zip(oxygen_criteria, map(lambda x: x == oxygen_rate, diagnostic))]
    try:
        (_, most_common), (co2_rate, least_common) = Counter(compress(diagnostic, co2_criteria)).most_common()
        if most_common == least_common:
            co2_rate = "0"
    except ValueError:
        co2_rate = next(compress(diagnostic, co2_criteria))
    co2_criteria = [x and y for x, y in zip(co2_criteria, map(lambda x: x == co2_rate, diagnostic))]

    oxygen_rating += oxygen_rate
    co2_rating += co2_rate
print("answer 2:", int(oxygen_rating, 2) * int(co2_rating, 2))
