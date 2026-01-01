try:
    product_ranges = open("inputs/day02.txt").read()
except FileNotFoundError:
    product_ranges = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""[1:]
product_ranges = product_ranges.split(",")

invalid_ids = set(int(str(i) + str(i)) for i in range(100_000))
total = 0
for product_range in product_ranges:
    start, end = product_range.split("-")
    found = invalid_ids.intersection(set(range(int(start), int(end) + 1)))
    total += sum(found)
print("answer 1:", total)

invalid_ids = set(int("".join([str(i)] * count)) for i in range(100_000) for count in range(2, 11))
total = 0
for product_range in product_ranges:
    start, end = product_range.split("-")
    found = invalid_ids.intersection(set(range(int(start), int(end) + 1)))
    total += sum(found)
print("answer 2:", total)
