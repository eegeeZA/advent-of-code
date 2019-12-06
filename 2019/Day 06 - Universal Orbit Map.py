orbits = {}
for my_orbit in open("inputs/day06.txt"):
    centre, around = my_orbit.strip().split(")")
    orbits[around] = centre


def count_orbits(find, count=0):
    if find in orbits:
        return count_orbits(orbits[find], count + 1)
    return count


print("answer 1:", sum([count_orbits(orbit) for orbit in orbits]))


def find_orbits(find, found):
    if find in orbits:
        return find_orbits(orbits[find], found + [orbits[find]])
    return found


my_orbits = find_orbits("YOU", [])
santa_orbits = find_orbits("SAN", [])
for my_orbit in my_orbits:
    if my_orbit in santa_orbits:
        print("answer 2:", my_orbits.index(my_orbit) + santa_orbits.index(my_orbit))
        break
