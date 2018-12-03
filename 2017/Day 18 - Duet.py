from collections import Counter

instructions = open("inputs/day18.txt").readlines()

i = 0
c = Counter()
frequency = None
while True:
    action, x, *y = instructions[i].split()
    i += 1
    if action == "rcv":
        if c[x] != 0:
            break
        continue
    if action == "snd":
        frequency = c[x]
        continue

    y = y.pop()
    y = int(y) if y.lstrip("-").isdigit() else c[y]
    if action == "set":
        c[x] = y
    if action == "add":
        c[x] += y
    if action == "mul":
        c[x] *= y
    if action == "mod":
        c[x] %= y
    if action == "jgz" and c[x] > 0:
        i += y - 1
print("answer 1:", frequency)


class Program:
    def __init__(self, pid):
        self.i = 0
        self.c = Counter()
        self.c["p"] = pid

        self.inbound = []
        self.outbound = None
        self.send_count = 0

    def run_until_wait(self):
        while True:
            action, x, *y = instructions[self.i].split()
            self.i += 1
            if action == "rcv":
                if len(self.inbound) == 0:
                    self.i -= 1
                    return
                self.c[x] = self.inbound.pop(0)
                continue
            if action == "snd":
                self.outbound.append(self.c[x])
                self.send_count += 1
                continue

            y = y.pop()
            y = int(y) if y.lstrip("-").isdigit() else self.c[y]
            if action == "set":
                self.c[x] = y
            if action == "add":
                self.c[x] += y
            if action == "mul":
                self.c[x] *= y
            if action == "mod":
                self.c[x] %= y

            x = int(x) if x.lstrip("-").isdigit() else self.c[x]  # oops
            if action == "jgz" and x > 0:
                self.i += y - 1


p0 = Program(0)
p1 = Program(1)
p0.outbound = p1.inbound
p1.outbound = p0.inbound
while True:
    p0.run_until_wait()
    p1.run_until_wait()
    if len(p0.inbound) == 0 and len(p1.inbound) == 0:
        break
print("answer 2:", p1.send_count)
