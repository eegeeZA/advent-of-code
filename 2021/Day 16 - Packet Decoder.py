import itertools
import math

try:
    bits = open("inputs/day16.txt").read().strip()
except FileNotFoundError:
    bits = "A0016C880162017C3686B18A3D4780"


def version_totals(binary):
    version = int(binary[:3], 2)
    packet_type = int(binary[3:6], 2)

    if packet_type == 4:
        literal = ""
        for i in itertools.count():
            part = binary[6 + i * 5:6 + (i + 1) * 5]
            literal += part[1:]
            if part[0] == "0":
                return version, binary[6 + (i + 1) * 5:], int(literal, 2)

    numbers = []
    if binary[6] == "0":
        sub_length = int(binary[7:7 + 15], 2)
        sub_packet = binary[7 + 15:7 + 15 + sub_length]
        binary = binary[7 + 15 + sub_length:]
        while sub_packet:
            sub_version, sub_packet, number = version_totals(sub_packet)
            version += sub_version
            numbers.append(number)
    elif binary[6] == "1":
        sub_count = int(binary[7:7 + 11], 2)
        binary = binary[7 + 11:]
        for _ in range(sub_count):
            sub_version, binary, number = version_totals(binary)
            version += sub_version
            numbers.append(number)

    result = None
    if packet_type == 0:
        result = sum(numbers)
    elif packet_type == 1:
        result = math.prod(numbers)
    elif packet_type == 2:
        result = min(numbers)
    elif packet_type == 3:
        result = max(numbers)
    elif packet_type == 5:
        result = int(numbers[0] > numbers[1])
    elif packet_type == 6:
        result = int(numbers[0] < numbers[1])
    elif packet_type == 7:
        result = int(numbers[0] == numbers[1])
    return version, binary, result


version_total, _, evaluation = version_totals("".join(bin(int(char, 16))[2:].zfill(4) for char in bits))
print("answer 1:", version_total)
print("answer 2:", evaluation)
