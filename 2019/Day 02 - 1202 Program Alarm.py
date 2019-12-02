from itertools import count


def answer1(int_code):
    int_code = int_code.copy()
    for i in count(0, 4):
        if int_code[i] == 1:
            int_code[int_code[i + 3]] = int_code[int_code[i + 1]] + int_code[int_code[i + 2]]
        elif int_code[i] == 2:
            int_code[int_code[i + 3]] = int_code[int_code[i + 1]] * int_code[int_code[i + 2]]
        elif int_code[i] == 99:
            return int_code[0]
        else:
            exit(str.format("something went wrong (pos:{} value:{})", i, int_code[i]))


def answer2(int_code, expected_output):
    for noun in range(100):
        for verb in range(100):
            int_code[1] = noun
            int_code[2] = verb
            if answer1(int_code) == expected_output:
                return 100 * noun + verb


initial_int_code = list(map(int, open("inputs/day02.txt").read().split(",")))
initial_int_code[1] = 12
initial_int_code[2] = 2
print("answer 1:", answer1(initial_int_code))
print("answer 2:", answer2(initial_int_code, 19690720))
