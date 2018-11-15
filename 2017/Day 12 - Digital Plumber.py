pipes = open("inputs/day12.txt")
links = {}
for pipe in pipes:
    key, ids = pipe.rstrip().split(" <-> ")
    ids = list(ids.split(", "))
    links[key] = ids

search = "0"
seen = set(search)
unseen = set(links[search])
while len(unseen) > 0:
    search = unseen.pop()
    seen.add(search)
    unseen |= set(links[search])
    unseen -= seen

print("answer 1:", len(seen))

seen = set()
groups = 0
for key in links.keys():
    if key not in seen:
        groups += 1
    seen.add(key)
    unseen = set(links[key])
    while len(unseen) > 0:
        search = unseen.pop()
        seen.add(search)
        unseen |= set(links[search])
        unseen -= seen

print("answer 2:", groups)
