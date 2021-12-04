import itertools

bingo_system = iter(open("inputs/day04.txt").read().split("\n\n"))
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
