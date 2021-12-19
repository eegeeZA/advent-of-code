import copy
import itertools
import math

snailfish_numbers = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""[1:]
snailfish_numbers = open("inputs/day18.txt").read()


def find_paths(number, path=None):
    if path is None:
        path = []

    for i, part in enumerate(number):
        sub_path = path.copy()
        sub_path.append(i)
        if isinstance(part, list):
            yield from find_paths(part, sub_path)
        else:
            yield sub_path, part


def update_nested(number, path, value):
    section = number
    for i in path[:-1]:
        section = section[i]
    section[path[-1]] = value


def reduce(number):
    paths = list(find_paths(number))

    for i, (path, value) in enumerate(paths):
        if len(path) > 4:
            if i > 0:
                left_path, left_value = paths[i - 1]
                update_nested(number, left_path, left_value + value)
            if i < len(paths) - 2:
                path, value = paths[i + 1]
                right_path, right_value = paths[i + 2]
                update_nested(number, right_path, right_value + value)
            update_nested(number, path[:-1], 0)
            return True

    for i, (path, value) in enumerate(paths):
        if value >= 10:
            update_nested(number, path, [value // 2, math.ceil(value / 2)])
            return True

    return False


def magnitude(number):
    result = 0

    left, right = number
    if isinstance(left, list):
        result += 3 * magnitude(left)
    else:
        result += 3 * left
    if isinstance(right, list):
        result += 2 * magnitude(right)
    else:
        result += 2 * right

    return result


parsed_numbers = list(map(eval, snailfish_numbers.splitlines()))
final_answer = parsed_numbers[0]
for snailfish_number in parsed_numbers[1:]:
    new_answer = [final_answer, snailfish_number]
    while reduce(new_answer):
        pass
    final_answer = new_answer
print("answer 1:", magnitude(final_answer))

max_magnitude = 0
parsed_numbers = list(map(eval, snailfish_numbers.splitlines()))
for combo in itertools.permutations(parsed_numbers, 2):
    combo = copy.deepcopy(combo)
    while reduce(combo):
        pass
    max_magnitude = max(max_magnitude, magnitude(combo))
print("answer 2:", max_magnitude)
