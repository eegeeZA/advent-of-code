import math

input_square = 289326
abs_distance = 0
square = 1
while math.pow(square, 2) < input_square:
    abs_distance += 1
    square += 2
corners = list(range(int(math.pow(square, 2)), int(math.pow(square - 2, 2)), -(square - 1)))
closest_corner = min(corners, key=lambda corner: abs(corner - input_square))
print("answer 1:", abs_distance * 2 - abs(closest_corner - input_square))


# Excel ftw
# 363010  349975  330785  312453  295229  279138  266330  130654
# 6591    6444    6155    5733    5336    5022    2450    128204
# 13486   147     142     133     122     59      2391    123363
# 14267   304     5       4       2       57      2275    116247
# 15252   330     10      1       1       54      2105    109476
# 16295   351     11      23      25      26      1968    103128
# 17008   362     747     806     880     931     957     98098
# 17370   35487   37402   39835   42452   45220   47108   48065
print("answer 2:", 295229)
