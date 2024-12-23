import collections
import itertools

try:
    puzzle = open("inputs/day23.txt").read()
except FileNotFoundError:
    puzzle = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""[1:]
puzzle = puzzle.splitlines()

connections = collections.defaultdict(set)
pairs = set()
for line in puzzle:
    a, b = line.split("-")
    connections[a].add(b)
    connections[b].add(a)
    pairs.add(frozenset([a, b]))

overlap = set()
for connection1 in connections:
    for connection2 in connections[connection1] - {connection1}:
        for connection3 in connections[connection2] - {connection1, connection2}:
            if (connection1 in connections[connection3]
                    and any(x.startswith('t') for x in {connection1, connection2, connection3})):
                overlap.add(frozenset([connection1, connection2, connection3]))
print("answer 1:", len(overlap))

networks = [{connection} for connection in connections]
for connection1 in connections:
    for network in networks:
        if all(frozenset([connection1, connection2]) in pairs for connection2 in network):
            network.add(connection1)
print("answer 2:", ','.join(sorted(sorted(networks, key=len)[-1])))
