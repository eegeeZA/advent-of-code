from collections import Counter

valid_passwords1 = 0
valid_passwords2 = 0
for password_policy in open("inputs/day02.txt"):
    policy, letter, password = password_policy.split()
    policy_min, policy_max = map(int, policy.split("-"))
    letter = letter.rstrip(":")

    if policy_min <= Counter(password)[letter] <= policy_max:
        valid_passwords1 += 1

    if (password[policy_min - 1] == letter) ^ (password[policy_max - 1] == letter):
        valid_passwords2 += 1

print("answer 1:", valid_passwords1)
print("answer 2:", valid_passwords2)
