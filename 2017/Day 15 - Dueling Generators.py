factor_a = 16807
factor_b = 48271
remainder = 2147483647

generator_a = 289
generator_b = 629
pairs = 0
for _ in range(40_000_000):
    generator_a = generator_a * factor_a % remainder
    generator_b = generator_b * factor_b % remainder
    if bin(generator_a)[-16:] == bin(generator_b)[-16:]:
        pairs += 1
print("answer 1:", pairs)

generator_a = 289
generator_b = 629
criteria_a = []
criteria_b = []
pairs = 0
while True:
    generator_a = generator_a * factor_a % remainder
    generator_b = generator_b * factor_b % remainder
    if generator_a % 4 == 0:
        criteria_a.append(bin(generator_a)[-16:])
    if generator_b % 8 == 0:
        criteria_b.append(bin(generator_b)[-16:])
    if len(criteria_a) >= len(criteria_b) >= 5_000_000:
        break
for a, b in zip(criteria_a, criteria_b):
    if a == b:
        pairs += 1
print("answer 2:", pairs)
