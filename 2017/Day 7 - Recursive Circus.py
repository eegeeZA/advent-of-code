def build_tree(tree, root):
    result = {root: []}
    if not tree[root]:
        return root
    for value in tree[root]:
        result[root].append(build_tree(tree, value))
    return result


def build_tree_weights(factor_x):
    if type(factor_x) is dict:
        for key, value in factor_x.items():
            return build_tree_weights(value)[0] + weights[key], key
    elif type(factor_x) is list:
        sub_values = []
        for value in factor_x:
            tree_weights = build_tree_weights(value)
            sub_values.append(tree_weights[0])
            if len(set(sub_values)) != 1:
                print(tree_weights, weights[tree_weights[1]])
                print(sub_values)
                exit()
        return sum(sub_values), ""
    else:
        return weights[factor_x], factor_x


inputs = open("inputs/day7.txt").read()
weights = {}
towers = {}
for line in str.splitlines(inputs):
    line_split = line.split(" -> ")
    name, weight = line_split[0].split(" ")
    weights[name] = int(weight[1:-1])
    if len(line_split) > 1:
        towers[name] = line_split[1].split(", ")
    else:
        towers[name] = []
root_key = ""
for k, v in towers.items():
    if inputs.count(k) == 1:
        root_key = k
print("answer 1:", root_key)
print("answer 2:",)
towers = build_tree(towers, root_key)
build_tree_weights(towers)
