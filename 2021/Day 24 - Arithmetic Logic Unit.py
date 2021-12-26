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


instructions = open("inputs/day24.txt").read().splitlines()
real_instructions = list(zip([int(z.split()[-1]) for z in instructions[4::18]],
                             [int(x.split()[-1]) for x in instructions[5::18]],
                             [int(y.split()[-1]) for y in instructions[15::18]]))
print("answer 1:", monad(real_instructions))
print("answer 2:", monad(real_instructions, False))
