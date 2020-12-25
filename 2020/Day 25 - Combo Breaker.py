from itertools import count

card, door = [int(x) for x in open("inputs/day25.txt")]

subject = 7
subject_number = 1
for i in count(1):
    subject_number *= subject
    subject_number %= 20201227
    if subject_number == card:
        subject = door
        break
    if subject_number == door:
        subject = card
        break

subject_number = 1
for _ in range(i):
    subject_number *= subject
    subject_number %= 20201227

print("answer 1:", subject_number)
print("answer 2:", "*")
