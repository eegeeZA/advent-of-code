from decimal import Decimal
from importlib import import_module

initial_int_code = list(map(int, open("inputs/day13.txt").read().split(",")))
initial_int_code[0] = 2
arcade = import_module("Day 09 - Sensor Boost").int_code_compute(initial_int_code)

block_tiles = ball_x = paddle_x = score = 0
while True:
    try:
        x = next(arcade)
        if x is None:
            x = arcade.send(Decimal(ball_x).compare(Decimal(paddle_x)))
        y = next(arcade)
        tile_id = next(arcade)

        if x == -1 and y == 0:
            score = tile_id
        elif tile_id == 2:
            block_tiles += 1
        elif tile_id == 3:
            paddle_x = x
        elif tile_id == 4:
            ball_x = x
    except StopIteration:
        break
print("answer 1:", block_tiles)
print("answer 2:", score)
