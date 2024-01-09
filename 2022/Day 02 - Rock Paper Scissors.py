try:
    strategy = open("inputs/day02.txt").readlines()
except FileNotFoundError:
    strategy = """A Y
B X
C Z""".splitlines()

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

score = 0
for turn in strategy:
    opp, me = turn.split()
    score += scores[me]
    if opp == 'A':
        if me == 'X':
            score += 3
        elif me == 'Y':
            score += 6
    if opp == 'B':
        if me == 'Y':
            score += 3
        elif me == 'Z':
            score += 6
    if opp == 'C':
        if me == 'Z':
            score += 3
        elif me == 'X':
            score += 6
print("answer 1:", score)

desired = {
    'X': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
    },
    'Y': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    },
    'Z': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
    },
}
score = 0
for turn in strategy:
    opp, me = turn.split()
    me = desired[me][opp]
    score += scores[me]
    if opp == 'A':
        if me == 'X':
            score += 3
        elif me == 'Y':
            score += 6
    if opp == 'B':
        if me == 'Y':
            score += 3
        elif me == 'Z':
            score += 6
    if opp == 'C':
        if me == 'Z':
            score += 3
        elif me == 'X':
            score += 6
print("answer 2:", score)
