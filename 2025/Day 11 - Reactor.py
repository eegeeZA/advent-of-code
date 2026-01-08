import collections
import functools

try:
    server_rack = open("inputs/day11.txt").read()
except FileNotFoundError:
    server_rack = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""[1:]
server_rack = server_rack.splitlines()


def count_paths(device_name, visited=None):
    if visited is None:
        visited = set()
    if device_name == "out":
        return True
    if device_name in visited:
        return False

    visited.add(device_name)

    total = 0
    for next_device in connections[device_name]:
        total += count_paths(next_device, visited.copy())

    return total


connections = collections.defaultdict(list)
for device in server_rack:
    source, targets = device.split(": ")
    connections[source] = targets.split()
print("answer 1:", count_paths("you"))


@functools.cache
def count_paths2(device_name, visited_dac, visited_fft):
    if device_name == "out":
        return visited_dac and visited_fft

    if device_name == "dac":
        visited_dac = 1
    if device_name == "fft":
        visited_fft = 1

    total = 0
    for next_device in connections[device_name]:
        total += count_paths2(next_device, visited_dac, visited_fft)

    return total


print("answer 2:", count_paths2("svr", 0, 0))
