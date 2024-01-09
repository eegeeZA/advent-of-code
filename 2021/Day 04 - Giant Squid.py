import itertools

try:
    bingo_system = iter(open("inputs/day04.txt").read().split("\n\n"))
except FileNotFoundError:
    bingo_system = iter("""
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".split("\n\n"))

draws = list(map(int, next(bingo_system).split(",")))

boards = []
for raw_board in bingo_system:
    rows = [list(map(int, x.split())) for x in raw_board.splitlines()]
    boards.append(rows + [list(x) for x in zip(*rows)])


def score(part2=False):
    for draw in draws:
        for board in boards:
            for row in board:
                if draw in row:
                    row.remove(draw)
                if not row:
                    boards.remove(board)
                    if part2 and boards:
                        return score(part2)
                    return draw * (sum(set(itertools.chain.from_iterable(board)) - {draw}))


print("answer 1:", score())
print("answer 2:", score(True))
