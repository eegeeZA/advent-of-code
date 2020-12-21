from collections import Counter

safe_ingredients = {}
allergens = {}
for line in open("inputs/day21.txt"):
    raw_ingredients, raw_allergens = line.rstrip().split(" (contains ")
    for confirmed_ingredient in raw_ingredients.split(" "):
        if confirmed_ingredient not in safe_ingredients:
            safe_ingredients[confirmed_ingredient] = Counter()
        safe_ingredients[confirmed_ingredient] += Counter(raw_allergens.rstrip(")").split(", ") + ["count"])
    for allergen in raw_allergens.rstrip(")").split(", "):
        if allergen not in allergens:
            allergens[allergen] = Counter()
        allergens[allergen] += Counter(raw_ingredients.split(" "))
dangerous = {}
for allergen in allergens:
    [(_, most_common)] = allergens[allergen].most_common(1)
    for confirmed_ingredient, count in allergens[allergen].items():
        if count == most_common:
            if confirmed_ingredient in safe_ingredients:
                del safe_ingredients[confirmed_ingredient]
            if allergen not in dangerous:
                dangerous[allergen] = []
            dangerous[allergen].append(confirmed_ingredient)
print("answer 1:", sum(ingredient["count"] for ingredient in safe_ingredients.values()))

confirmed_ingredients = []
while len(confirmed_ingredients) != len(dangerous):
    confirmed_ingredients = [ingredients[0] for ingredients in dangerous.values() if len(ingredients) == 1]
    for confirmed_ingredient in confirmed_ingredients:
        for ingredients in dangerous.values():
            if len(ingredients) > 1 and confirmed_ingredient in ingredients:
                ingredients.remove(confirmed_ingredient)
print("answer 2:", ",".join(dangerous[allergen][0] for allergen in sorted(dangerous)))
