from collections import Counter

count1 = 0
count2 = 0
answers1 = ""
answers2 = None
for line in open("inputs/day06.txt"):
    answers1 += line.strip()
    if answers2 is None:
        answers2 = set(line.strip())
    if line == "\n":
        count1 += len(Counter(answers1))
        count2 += len(answers2)
        answers1 = ""
        answers2 = None
    else:
        answers2 &= set(line.strip())

print("answer 1:", count1)
print("answer 2:", count2)
