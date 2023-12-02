import itertools
import re

games = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""[1:].splitlines()
games = open("inputs/day02.txt").read().splitlines()

valid_games = 0
for id, game in zip(itertools.count(1), games):
    for count, colour in re.findall(r"(\d+) (red|green|blue)", game):
        if colour == "red" and int(count) > 12:
            break
        if colour == "green" and int(count) > 13:
            break
        if colour == "blue" and int(count) > 14:
            break
    else:
        valid_games += id
print("answer 1:", valid_games)

power = 0
for game in games:
    red, green, blue = 0, 0, 0
    for count, colour in re.findall(r"(\d+) (red|green|blue)", game):
        if colour == "red":
            red = max(red, int(count))
        if colour == "green":
            green = max(green, int(count))
        if colour == "blue":
            blue = max(blue, int(count))
    power += red * green * blue
print("answer 2:", power)
