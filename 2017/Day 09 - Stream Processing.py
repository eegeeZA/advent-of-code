stream = open("inputs/day09.txt").readlines()[0]
score = 0
depth = 1
garbage = False
ignoreNext = False
garbageRemoved = 0
for char in stream:
    if ignoreNext:
        ignoreNext = False
    elif char == "!":
        ignoreNext = True
    elif char == "{" and not garbage:
        score += depth * 1
        depth += 1
    elif char == "}" and not garbage:
        depth -= 1
    elif char == "<" and not garbage:
        garbage = True
    elif char == ">":
        garbage = False
    elif garbage:
        garbageRemoved += 1
print("answer 1:", score)
print("answer 2:", garbageRemoved)
