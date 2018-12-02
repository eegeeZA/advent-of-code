from itertools import combinations

twos = 0
threes = 0
for box_id in open("inputs/day02.txt"):
    seen = []
    two_counted = three_counted = False
    for letter in box_id.rstrip():
        if letter in seen:
            continue
        else:
            seen.append(letter)

        count = box_id.count(letter)
        if count == 2 and not two_counted:
            twos += 1
            two_counted = True
        if count == 3 and not three_counted:
            threes += 1
            three_counted = True
print("answer 1:", twos * threes)

best = ""
for x, y in combinations(open("inputs/day02.txt"), 2):
    common_letters = ""
    for a, b in zip(x, y):
        if a == b:
            common_letters += a
    if len(common_letters) > len(best):
        best = common_letters
print("answer 2:", best)
