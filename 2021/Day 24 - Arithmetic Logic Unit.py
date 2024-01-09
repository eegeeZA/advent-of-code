try:
    instructions = open("inputs/day24.txt").read().splitlines()
    real_instructions = list(zip([int(z.split()[-1]) for z in instructions[4::18]],
                                 [int(x.split()[-1]) for x in instructions[5::18]],
                                 [int(y.split()[-1]) for y in instructions[15::18]]))
except FileNotFoundError:
    real_instructions = [
        (1, 13, 0),  # d[1]  +  0 -  1 == d[14] -> d[1] -  1 == d[14]   | 9  | 2
        (1, 11, 3),  # d[2]  +  3 -  9 == d[13] -> d[2] -  6 == d[13]   | 9  | 7
        (1, 14, 8),  # d[3]  +  8 -  5 == d[4]  -> d[3] +  3 == d[4]    | 6  | 1
        (26, -5, 5),  # d[4]  -  8 +  5 == d[3]  -> d[4] -  3 == d[3]    | 9  | 4
        (1, 14, 13),  # d[5]  + 13 -  5 == d[12] -> d[5] +  8 == d[12]   | 1  | 1
        (1, 10, 9),  # d[6]  +  9 -  8 == d[9]  -> d[6] +  1 == d[9]    | 8  | 1
        (1, 12, 6),  # d[7]  +  6 - 14 == d[8]  -> d[7] -  8 == d[8]    | 9  | 9
        (26, -14, 1),  # d[8]  -  6 + 14 == d[7]  -> d[8] +  8 == d[7]    | 1  | 1
        (26, -8, 1),  # d[9]  -  9 +  8 == d[6]  -> d[9] -  1 == d[6]    | 9  | 2
        (1, 13, 2),  # d[10] +  2 -  0 == d[11] -> d[10] + 2 == d[11]   | 7  | 1
        (26, 0, 7),  # d[11] -  2 +  0 == d[10] -> d[11] - 2 == d[10]   | 9  | 3
        (26, -5, 5),  # d[12] - 13 +  5 == d[5]  -> d[12] - 8 == d[5]    | 9  | 9
        (26, -9, 8),  # d[13] -  3 +  9 == d[2]  -> d[13] + 6 == d[2]    | 3  | 1
        (26, -1, 15)  # d[14] -  0 +  1 == d[1]  -> d[14] + 1 == d[1]    | 8  | 1
    ]


def monad(operations, largest=True, final_z=0, answer=None):
    if answer is None:
        answer = []
    if not operations:
        if final_z == 0:
            return "".join(map(str, answer))
        else:
            return

    z, x, y = operations[0]
    if z == 26:
        if 1 <= (final_z % 26) + x <= 9:
            return monad(operations[1:], largest, final_z // z, answer + [(final_z % 26) + x])
        return

    for w in (range(9, 0, -1) if largest else range(1, 10)):
        result = monad(operations[1:], largest, final_z // z * 26 + w + y, answer + [w])
        if result:
            return result


print("answer 1:", monad(real_instructions))
print("answer 2:", monad(real_instructions, False))
