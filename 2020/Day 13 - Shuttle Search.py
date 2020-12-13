import math

earliest, raw_bus_ids = open("inputs/day13.txt").readlines()
earliest = int(earliest)
bus_ids = [int(bus_id) for bus_id in raw_bus_ids.split(",") if bus_id != "x"]

lowest_time = max(bus_ids)
lowest_bus_id = None
for bus_id in bus_ids:
    if (bus_id - earliest % bus_id) < lowest_time:
        lowest_time = bus_id - earliest % bus_id
        lowest_bus_id = bus_id
print("answer 1:", lowest_time * lowest_bus_id)


def chinese_remainder_theorem(mods, remainders):
    result = 0
    for mod, remainder in zip(mods, remainders):
        big_n = math.prod(mods) // mod
        for inverse in range(mod):
            if big_n * inverse % mod == 1:
                result += remainder * big_n * inverse
                break
    return result % math.prod(mods)


positions = [int(bus_id) - i for i, bus_id in enumerate(raw_bus_ids.split(",")) if bus_id != "x"]
print("answer 2:", chinese_remainder_theorem(bus_ids, positions))
