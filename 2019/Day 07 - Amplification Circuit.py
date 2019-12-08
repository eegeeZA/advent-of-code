from importlib import import_module
from itertools import permutations

x = import_module("Day 05 - Sunny with a Chance of Asteroids")
initial_int_code = list(map(int, open("inputs/day07.txt").read().split(",")))

max_signal = 0
for phase in permutations(range(5)):
    input_signal = 0
    for amp in range(5):
        input_signal = x.int_code_compute(initial_int_code, [phase[amp], input_signal])
    max_signal = max(max_signal, input_signal)
print("answer 1:", max_signal)
