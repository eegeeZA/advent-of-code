almanac = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""[1:].split("\n\n")
almanac = open("inputs/day05.txt").read().split("\n\n")

seeds = list(map(int, almanac[0].split()[1:]))
seed_ranges = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
for mapping in almanac[1:]:
    ranges = [list(map(int, triplets.split())) for triplets in mapping.splitlines()[1:]]
    for i, seed in enumerate(seeds):
        for destination, source, length in ranges:
            if seed in range(source, source + length):
                seeds[i] = (destination - source) + seed
                break
print("answer 1:", min(seeds))

final = []
for mapping in almanac[1:]:
    ranges = [list(map(int, triplets.split())) for triplets in mapping.splitlines()[1:]]
    new_ranges = []
    while final:
        final_destination, final_source, final_length = final.pop()
        for i in reversed(range(len(ranges))):
            destination, source, length = ranges[i]
            overlap = range(max(final_destination, source), min(final_destination + final_length, source + length))
            if overlap:
                del ranges[i]
                new_ranges.append(
                    [destination + (overlap.start - source), final_source + (overlap.start - final_destination),
                     len(overlap)])
                if source < overlap.start:
                    ranges.append([destination, source, overlap.start - source])
                if (source + length) > overlap.stop:
                    ranges.append([destination + len(overlap) + (overlap.start - source),
                                   source + len(overlap) + (overlap.start - source),
                                   length - (overlap.start - source) - len(overlap)])
                if final_destination < overlap.start:
                    final.append([final_destination, final_source, overlap.start - final_destination])
                if (final_destination + final_length) > overlap.stop:
                    final.append([final_destination + len(overlap) + (overlap.start - final_destination),
                                  final_source + len(overlap) + (overlap.start - final_destination),
                                  final_length - (overlap.start - final_destination) - len(overlap)])
                break
        else:
            new_ranges.append([final_destination, final_source, final_length])
    final = new_ranges + ranges

lowest = None
for destination, source, length in sorted(final):
    for seed in seed_ranges:
        overlap = range(max(source, seed.start), min(source + length, seed.stop))
        if overlap:
            lowest = range(destination, destination + length)[
                range(source, source + length).index(overlap.start)]
            break
    if lowest:
        break
print("answer 2:", lowest)
