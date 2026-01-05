from itertools import combinations

try:
    red_tiles = open("inputs/day09.txt").read()
except FileNotFoundError:
    red_tiles = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""[1:]
red_tiles = [tuple(map(int, line.split(','))) for line in red_tiles.splitlines()]

def area(a, b):
    (ax, ay), (bx, by) = a, b
    return (abs(ax - bx) + 1) * (abs(ay - by) + 1)

print("answer 1:", max(area(a, b) for a, b in combinations(red_tiles, 2)))

vertical = []
horizontal = []
for i in range(len(red_tiles)):
    (ax, ay), (bx, by) = red_tiles[i], red_tiles[(i + 1) % len(red_tiles)]
    if ax == bx:
        vertical.append((ax, min(ay, by), max(ay, by)))
    else:
        horizontal.append((ay, min(ax, bx), max(ax, bx)))

def inside(x, y):
    if any(y == hy and hx_start <= x <= hx_end for hy, hx_start, hx_end in horizontal):
        return True
    if any(x == vx and vy_start <= y <= vy_end for vx, vy_start, vy_end in vertical):
        return True
    return sum(1 for vx, vy_start, vy_end in vertical if vx > x and vy_start < y < vy_end) % 2 == 1

def valid(a, b):
    (ax, ay), (bx, by) = a, b
    x1, x2 = min(ax, bx), max(ax, bx)
    y1, y2 = min(ay, by), max(ay, by)
    if not all(inside(x, y) for x, y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]):
        return False
    if any(x1 < vx < x2 and max(vy_start, y1) < min(vy_end, y2) for vx, vy_start, vy_end in vertical):
        return False
    if any(y1 < hy < y2 and max(hx_start, x1) < min(hx_end, x2) for hy, hx_start, hx_end in horizontal):
        return False
    return True

pairs = sorted(combinations(red_tiles, 2), key=lambda x: -area(*x))
print("answer 2:", next(area(a, b) for a, b in pairs if valid(a, b)))
