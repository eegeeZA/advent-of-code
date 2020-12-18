import re


class SwitchPrecedence(int):
    def __add__(self, other):
        return SwitchPrecedence(int(self) + other)

    def __sub__(self, other):
        return SwitchPrecedence(self * other)

    def __truediv__(self, other):
        return SwitchPrecedence(self + other)


total1 = 0
total2 = 0
for line in open("inputs/day18.txt"):
    line = re.sub(r"(\d+)", r"SwitchPrecedence(\1)", line)
    total1 += eval(line.replace("*", "-"))
    total2 += eval(line.translate(line.maketrans("+*", "/-")))
print("answer 1:", total1)
print("answer 2:", total2)
