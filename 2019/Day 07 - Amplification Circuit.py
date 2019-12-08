from importlib import import_module
from itertools import permutations, cycle

x = import_module("Day 05 - Sunny with a Chance of Asteroids")
initial_int_code = list(map(int, open("inputs/day07.txt").read().split(",")))

max_signal = 0
for phase in permutations(range(5)):
    amplifiers = []
    for i in range(5):
        amplifier = x.int_code_compute(initial_int_code)
        amplifiers.append(amplifier)
        next(amplifier)
        amplifier.send(phase[i])
    input_signal = 0
    for amplifier in amplifiers:
        input_signal = amplifier.send(input_signal)
    max_signal = max(max_signal, input_signal)
print("answer 1:", max_signal)

max_signal = 0
for phase in permutations(range(5, 10)):
    amplifiers = []
    for i in range(5):
        amplifier = x.int_code_compute(initial_int_code)
        amplifiers.append(amplifier)
        next(amplifier)
        amplifier.send(phase[i])
    input_signal = 0
    for amplifier in cycle(amplifiers):
        try:
            signal = amplifier.send(input_signal)
        except StopIteration:
            break
        if signal is not None:
            input_signal = signal
    max_signal = max(max_signal, input_signal)
print("answer 2:", max_signal)
