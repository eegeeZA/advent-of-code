import collections
import functools
import itertools

try:
    players = open("inputs/day21.txt").read()
except FileNotFoundError:
    players = """
Player 1 starting position: 4
Player 2 starting position: 8
"""[1:]

player_scores = [0, 0]
player_positions = [int(player[-1]) for player in players.splitlines()]
deterministic_die = iter(itertools.cycle(range(1, 100 + 1)))
for die_rolls in itertools.count():
    player_positions[die_rolls % 2] += next(deterministic_die)
    player_positions[die_rolls % 2] += next(deterministic_die)
    player_positions[die_rolls % 2] += next(deterministic_die)

    player_positions[die_rolls % 2] = ((player_positions[die_rolls % 2] - 1) % 10) + 1
    player_scores[die_rolls % 2] += player_positions[die_rolls % 2]

    if player_scores[die_rolls % 2] >= 1000:
        die_rolls += 1
        break
print("answer 1:", player_scores[die_rolls % 2] * die_rolls * 3)


@functools.cache
def roll_dirac_die(position1, position2, score1, score2):
    if score2 >= 21:
        return False, True

    wins1 = wins2 = 0

    for score, score_count in scores_outcomes:
        new_position1 = ((position1 + score - 1) % 10) + 1
        new_score1 = score1 + new_position1

        new_wins2, new_wins1 = roll_dirac_die(position2, new_position1, score2, new_score1)

        wins1 += new_wins1 * score_count
        wins2 += new_wins2 * score_count

    return wins1, wins2


player_positions = [int(player[-1]) for player in players.splitlines()]
scores_outcomes = collections.Counter(sum(rolls) for rolls in itertools.product(range(1, 3 + 1), repeat=3)).items()
print("answer 2:", max(roll_dirac_die(player_positions[0], player_positions[1], 0, 0)))
