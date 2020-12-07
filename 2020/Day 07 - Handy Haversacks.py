import re

rules = {}
for rule in open("inputs/day07.txt"):
    bag_type, rule = rule.split(" bags contain")
    bag_contains = rule.strip().rstrip(".").split(", ")
    rules[bag_type] = []
    for bag_contained in bag_contains:
        if bag_contained != "no other bags":
            rules[bag_type].append((int(bag_contained[0]), re.sub(r" bags?", "", str(bag_contained[2:]))))


def find_shiny_gold_bag(bag_name):
    result = False
    for count, sub_bag in rules[bag_name]:
        if sub_bag == "shiny gold":
            return True
        result |= find_shiny_gold_bag(sub_bag)
    return result


def count_bags(bag_name):
    result = 0
    for count, sub_bag in rules[bag_name]:
        result += count
        result += count * count_bags(sub_bag)
    return result


count_shiny_gold_bags = 0
for rule in rules:
    if find_shiny_gold_bag(rule):
        count_shiny_gold_bags += 1
print("answer 1:", count_shiny_gold_bags)
print("answer 2:", count_bags("shiny gold"))
