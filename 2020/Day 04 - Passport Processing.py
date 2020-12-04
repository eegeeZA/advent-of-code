import re

passports = []
passport = ""
for line in open("inputs/day04.txt"):
    passport += line
    if line == "\n":
        passports.append(passport)
        passport = ""
passports.append(passport)

valid_passports1 = 0
valid_passports2 = 0
for passport in passports:
    if not all(required_key in passport for required_key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
        continue
    valid_passports1 += 1

    valid_count = 0
    for key_value in passport.split():
        key, value = key_value.split(":")
        if "byr" == key and 1920 <= int(value) <= 2002:
            valid_count += 1
        if "iyr" == key and 2010 <= int(value) <= 2020:
            valid_count += 1
        if "eyr" == key and 2020 <= int(value) <= 2030:
            valid_count += 1
        if "hgt" == key and (("cm" in value and 150 <= int(value.replace("cm", "")) <= 193)
                             or ("in" in value and 59 <= int(value.replace("in", "")) <= 76)):
            valid_count += 1
        if "hcl" == key and re.match(r"^#[0-9a-f]{6}$", value):
            valid_count += 1
        if "ecl" == key and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            valid_count += 1
        if "pid" == key and re.match(r"^\d{9}$", value):
            valid_count += 1
    if valid_count == 7:
        valid_passports2 += 1

print("answer 1:", valid_passports1)
print("answer 2:", valid_passports2)
