firewall = open("inputs/day13.txt")
firewalls = []
for layer in firewall:
    depth, view_range = map(int, layer.split(": "))
    firewalls.append((depth, view_range))

severity = 0
for depth, view_range in firewalls:
    if depth % ((view_range * 2) - 2) == 0:
        severity += depth * view_range
print("answer 1:", severity)

delay = 0
while True:
    for depth, view_range in firewalls:
        offset = delay + depth
        if offset % ((view_range * 2) - 2) == 0:
            delay += 1
            break
    else:
        break
print("answer 2:", delay)
