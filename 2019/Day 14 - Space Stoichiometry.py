from collections import Counter
from math import ceil


def ore_required(required_quantity, chemical, total_costs):
    produced_quantity, ingredients = full_ingredients[chemical]

    savings = min(required_quantity, total_costs[chemical])
    required_quantity -= savings
    total_costs[chemical] -= savings

    quantity_multiplier = ceil(required_quantity / produced_quantity)
    total_costs[chemical] += (quantity_multiplier * produced_quantity) - required_quantity

    if "ORE" in ingredients:
        total_costs["ORE"] += ingredients["ORE"] * quantity_multiplier
    else:
        for ingredient, ingredient_quantity in ingredients.items():
            ore_required(quantity_multiplier * ingredient_quantity, ingredient, total_costs)

    return total_costs


full_ingredients = {}
for reaction in open("inputs/day14.txt"):
    chemical_inputs, chemical_output = reaction.strip().split(" => ")
    output_quantity, output_name = chemical_output.split(" ")
    reactions = {input_name: int(input_quantity) for input_quantity, input_name in
                 map(lambda x: x.split(" "), chemical_inputs.split(", "))}
    full_ingredients[output_name] = int(output_quantity), reactions

ore_cost = ore_required(1, "FUEL", Counter())["ORE"]
print("answer 1:", ore_cost)

fuel_produced = 0
while (add_fuel := (1000000000000 - ore_required(fuel_produced, "FUEL", Counter())["ORE"]) // ore_cost) > 0:
    fuel_produced += add_fuel
print("answer 2:", fuel_produced)
