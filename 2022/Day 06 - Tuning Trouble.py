try:
    signal = open("inputs/day06.txt").read()
except FileNotFoundError:
    signal = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

for i in range(len(signal)):
    if len(set(signal[i:i + 4])) == 4:
        print("answer 1:", i + 4)
        break

for i in range(len(signal)):
    if len(set(signal[i:i + 14])) == 14:
        print("answer 2:", i + 14)
        break
