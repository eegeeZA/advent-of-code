import turtle
from collections import Counter
from importlib import import_module

initial_int_code = list(map(int, open("inputs/day11.txt").read().split(",")))
painter = import_module("Day 09 - Sensor Boost").int_code_compute(initial_int_code)

space_hull = Counter()
space_hull[0, 0] = 1

painter_bot = turtle.Turtle()
painter_bot.speed(0)
painter_bot.setheading(90)

while True:
    try:
        next(painter)
        current_colour = 0 if painter_bot.position() not in space_hull else space_hull[painter_bot.position()]
        new_colour = painter.send(current_colour)
        new_direction = next(painter)
    except StopIteration:
        break
    space_hull[painter_bot.position()] = new_colour
    painter_bot.dot(10, "white" if new_colour == 0 else "black")

    if new_direction == 0:
        painter_bot.left(90)
    elif new_direction == 1:
        painter_bot.right(90)
    painter_bot.forward(10)

turtle.Screen().exitonclick()
