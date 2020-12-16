is_start = True
is_yours = False
is_nearby = False
all_valid_ranges = []
error_rate = 0
valid_fields = []
for line in open("inputs/day16.txt"):
    if line == "\n":
        if is_start:
            is_start = False
            is_yours = True
        elif is_yours:
            is_yours = False
            is_nearby = True
        continue
    if is_start:
        field, valid_ranges = line.split(":")
        all_valid_ranges.append((field, [valid_range.split("-") for valid_range in valid_ranges.split("or")]))
        valid_fields.append(field)
    if is_yours and "your" not in line:
        yours = [int(x) for x in line.split(",")]
        valid_fields = [valid_fields.copy() for _ in range(len(yours))]
    if is_nearby and "nearby" not in line:
        all_valid = True
        for number in line.split(","):
            valid = False
            for field, valid_ranges in all_valid_ranges:
                for start, end in valid_ranges:
                    if int(start) <= int(number) <= int(end):
                        valid = True
            if not valid:
                error_rate += int(number)
                all_valid = False
        if all_valid:
            for i, number in enumerate(line.split(",")):
                for field, valid_ranges in all_valid_ranges:
                    valid = False
                    for start, end in valid_ranges:
                        if int(start) <= int(number) <= int(end):
                            valid = True
                    if not valid and field in valid_fields[i]:
                        valid_fields[i].remove(field)
print("answer 1:", error_rate)

for [sorted_field] in sorted(valid_fields, key=len):
    for valid_field in valid_fields:
        if len(valid_field) > 1 and sorted_field in valid_field:
            valid_field.remove(sorted_field)
departures = 1
for i, [field] in enumerate(valid_fields):
    if field.startswith("departure"):
        departures *= yours[i]
print("answer 2:", departures)
