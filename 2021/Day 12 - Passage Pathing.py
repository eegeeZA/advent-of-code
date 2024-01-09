import collections

try:
    caves = open("inputs/day12.txt").read().splitlines()
except FileNotFoundError:
    caves = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]

paths = collections.defaultdict(list)
for cave in caves:
    start, end = cave.split("-")
    paths[start].append(end)
    paths[end].append(start)


def end_routes(path_name, extra_visit=False, visited_caves=None):
    if visited_caves is None:
        visited_caves = set()

    if path_name == "end":
        yield True

    visited_caves.add(path_name)
    for route in paths[path_name]:
        if route.islower() and route in visited_caves:
            if extra_visit and route not in ["start", "end"]:
                yield from end_routes(route, False, visited_caves.copy())
            continue
        yield from end_routes(route, extra_visit, visited_caves.copy())


print("answer 1:", sum(end_routes("start")))
print("answer 2:", sum(end_routes("start", True)))
