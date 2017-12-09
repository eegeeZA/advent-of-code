captcha = open("inputs/day1.txt").readlines()[0]
answer = 0
for i, char in enumerate(captcha):
    if char == captcha[(i + 1) % len(captcha)]:
        answer += int(char)
print("answer 1:", answer)

answer = 0
for i, char in enumerate(captcha):
    if char == captcha[(i + len(captcha) // 2) % len(captcha)]:
        answer += int(char)
print("answer 2:", answer)
