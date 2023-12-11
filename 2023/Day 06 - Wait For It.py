paper_sheet = """
Time:      7  15   30
Distance:  9  40  200
"""[1:].splitlines()
paper_sheet = """
Time:        40     92     97     90
Distance:   215   1064   1505   1100
"""[1:].splitlines()

times, distances = (list(map(int, line.split()[1:])) for line in paper_sheet)
ways_to_beat = 1
for time, distance in zip(times, distances):
    ways_to_beat *= sum((hold * (time - hold)) > distance for hold in range(1, time))
print("answer 1:", ways_to_beat)

time, distance = (int("".join(line.split()[1:])) for line in paper_sheet)
print("answer 2:", sum((hold * (time - hold)) > distance for hold in range(1, time)))
