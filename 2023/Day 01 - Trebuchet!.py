import re

calibrations = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""[1:].splitlines()
calibrations = open("inputs/day01.txt").read().splitlines()

integers = [re.findall(r"\d", x) for x in calibrations]
print("answer 1:", sum(int(x[0] + x[-1]) for x in integers))

integers = []
translations = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e",
                "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
for calibration in calibrations:
    for key, value in translations.items():
        calibration = calibration.replace(key, value)
    integers.append(re.findall(r"\d", calibration))
print("answer 2:", sum(int(x[0] + x[-1]) for x in integers))
