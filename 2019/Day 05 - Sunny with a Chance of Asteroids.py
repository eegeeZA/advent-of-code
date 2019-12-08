def lookup(int_code, mode, index):
    if mode == "0":
        return int_code[int_code[index]]
    elif mode == "1":
        return int_code[index]
    else:
        exit(str.format("something went wrong (mode:{} index:{})", mode, index))


def int_code_compute(int_code):
    int_code = int_code.copy()
    i = 0
    while True:
        a, b, c, *de = str(int_code[i]).rjust(5, "0")
        op_code = "".join(de)

        if op_code == "01":
            int_code[int_code[i + 3]] = lookup(int_code, c, i + 1) + lookup(int_code, b, i + 2)
            i += 4
        elif op_code == "02":
            int_code[int_code[i + 3]] = lookup(int_code, c, i + 1) * lookup(int_code, b, i + 2)
            i += 4
        elif op_code == "03":
            int_code[int_code[i + 1]] = yield
            i += 2
        elif op_code == "04":
            yield lookup(int_code, c, i + 1)
            i += 2
        elif op_code == "05":
            if lookup(int_code, c, i + 1) != 0:
                i = lookup(int_code, b, i + 2)
            else:
                i += 3
        elif op_code == "06":
            if lookup(int_code, c, i + 1) == 0:
                i = lookup(int_code, b, i + 2)
            else:
                i += 3
        elif op_code == "07":
            int_code[int_code[i + 3]] = 1 if lookup(int_code, c, i + 1) < lookup(int_code, b, i + 2) else 0
            i += 4
        elif op_code == "08":
            int_code[int_code[i + 3]] = 1 if lookup(int_code, c, i + 1) == lookup(int_code, b, i + 2) else 0
            i += 4
        elif op_code == "99":
            break
        else:
            exit(str.format("something went wrong (pos:{} value:{})", i, op_code))

    return


if __name__ == "__main__":
    initial_int_code = list(map(int, open("inputs/day05.txt").read().split(",")))
    answer1 = int_code_compute(initial_int_code)
    next(answer1)
    answer1.send(1)
    print("answer 1:", max(answer1))
    answer2 = int_code_compute(initial_int_code)
    next(answer2)
    print("answer 2:", answer2.send(5))
