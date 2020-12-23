cups = [int(x) for x in open("inputs/day23.txt").read().rstrip()]
current = cups[0]
for _ in range(100):
    current_index = cups.index(current)
    picks = []
    for pick in range(3):
        picks.append(cups[(current_index + pick + 1) % len(cups)])
    for pick in picks:
        cups.remove(pick)

    destination = current - 1
    while destination in [0] + picks:
        destination -= 1
        if destination <= 0:
            destination = max(cups)

    destination = cups.index(destination)
    cups = cups[:destination + 1] + picks + cups[destination + 1:]
    current = cups[(cups.index(current) + 1) % len(cups)]
print("answer 1:", "".join([str(cups[i % len(cups)]) for i in range(cups.index(1) + 1, cups.index(1) + len(cups))]))

cups = [int(x) for x in open("inputs/day23.txt").read().rstrip()]
current = cups[0]
cups += range(max(cups) + 1, 1000000 + 1)
cups = {cups[i - 1]: cup for i, cup in enumerate(cups)}
for _ in range(10000000):
    picks = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]

    destination = current - 1
    while destination in [0] + picks:
        destination -= 1
        if destination <= 0:
            destination = max(cups)

    cups[current] = current = cups[picks[-1]]
    cups[destination], cups[picks[-1]] = picks[0], cups[destination]
print("answer 2:", cups[1] * cups[cups[1]])
