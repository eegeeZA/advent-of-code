from collections import Counter

relative_base = 0


def lookup(int_code, i, offset):
    modes = str(int_code[i]).rjust(5, "0")
    if modes[3 - offset] == "0":
        return int_code[i + offset]
    elif modes[3 - offset] == "1":
        return i + offset
    elif modes[3 - offset] == "2":
        return relative_base + int_code[i + offset]
    else:
        exit(str.format("something went wrong (modes:{} index:{})", modes, offset))


def int_code_compute(int_code):
    int_code = Counter({i: val for i, val in enumerate(int_code)})
    i = 0
    global relative_base
    relative_base = 0
    while True:
        op_code = str(int_code[i]).rjust(2, "0")[-2:]

        if op_code == "01":
            int_code[lookup(int_code, i, 3)] = int_code[lookup(int_code, i, 1)] + int_code[lookup(int_code, i, 2)]
            i += 4
        elif op_code == "02":
            int_code[lookup(int_code, i, 3)] = int_code[lookup(int_code, i, 1)] * int_code[lookup(int_code, i, 2)]
            i += 4
        elif op_code == "03":
            int_code[lookup(int_code, i, 1)] = yield
            i += 2
        elif op_code == "04":
            yield int_code[lookup(int_code, i, 1)]
            i += 2
        elif op_code == "05":
            if int_code[lookup(int_code, i, 1)] != 0:
                i = int_code[lookup(int_code, i, 2)]
            else:
                i += 3
        elif op_code == "06":
            if int_code[lookup(int_code, i, 1)] == 0:
                i = int_code[lookup(int_code, i, 2)]
            else:
                i += 3
        elif op_code == "07":
            if int_code[lookup(int_code, i, 1)] < int_code[lookup(int_code, i, 2)]:
                int_code[lookup(int_code, i, 3)] = 1
            else:
                int_code[lookup(int_code, i, 3)] = 0
            i += 4
        elif op_code == "08":
            if int_code[lookup(int_code, i, 1)] == int_code[lookup(int_code, i, 2)]:
                int_code[lookup(int_code, i, 3)] = 1
            else:
                int_code[lookup(int_code, i, 3)] = 0
            i += 4
        elif op_code == "09":
            relative_base += int_code[lookup(int_code, i, 1)]
            i += 2
        elif op_code == "99":
            break
        else:
            exit(str.format("something went wrong (pos:{} value:{})", i, op_code))

    return


if __name__ == "__main__":
    initial_int_code = list(map(int, open("inputs/day09.txt").read().split(",")))
    answer1 = int_code_compute(initial_int_code)
    next(answer1)
    print("answer 1:", answer1.send(1))
    answer2 = int_code_compute(initial_int_code)
    next(answer2)
    print("answer 2:", answer2.send(2))
