from collections import Counter

valid_passwords = 0
valid_passwords2 = 0
for password in range(272091, 815432):
    password_string = str(password)
    double = False
    ascending = True
    for i in range(len(password_string) - 1):
        if password_string[i] == password_string[i + 1]:
            double = True
        if int(password_string[i]) > int(password_string[i + 1]):
            ascending = False
    if double and ascending:
        valid_passwords += 1
        for number, occurrence in Counter(password_string).most_common():
            if occurrence == 2:
                valid_passwords2 += 1
                break
print("answer 1:", valid_passwords)
print("answer 1:", valid_passwords2)
