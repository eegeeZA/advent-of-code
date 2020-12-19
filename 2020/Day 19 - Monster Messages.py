import re

rules = {}
input_file = open("inputs/day19.txt")
for line in input_file:
    if line == "\n":
        break
    i, raw_rules = line.split(":")
    i = int(i)
    if '"' in raw_rules:
        rules[i] = raw_rules.replace('"', "").strip()
    else:
        rules[i] = []
        for x in raw_rules.split("|"):
            rule = []
            for y in x.split():
                rule.append((int(y)))
            rules[i].append(rule)
received_messages = [line.rstrip() for line in input_file]


def regex_rules(rule_index=0):
    results = []
    for rule_group in rules[rule_index]:
        group_results = ""
        for group_index in rule_group:
            if isinstance(rules[group_index], list):
                group_results += "(" + regex_rules(group_index) + ")"
            else:
                group_results += rules[group_index]
        results.append(group_results)
    return "|".join(results)


regex = "^{0}$".format(regex_rules())
print("answer 1:", sum([bool(re.match(regex, received_message)) for received_message in received_messages]))

rules[8] = [[42] * x for x in range(1, 10)]
rules[11] = [[42] * x + [31] * x for x in range(1, 10)]
regex = "^{0}$".format(regex_rules())
print("answer 2:", sum([bool(re.match(regex, received_message)) for received_message in received_messages]))
