import collections
import functools

hands = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""[1:].splitlines()
hands = open("inputs/day07.txt").read().splitlines()


def strength(hand):
    kinds = collections.Counter(hand).values()
    if max(kinds) >= 4:
        return max(kinds) + 1
    if max(kinds) == 3:
        if min(kinds) == 2:
            return 4
        else:
            return 3
    if sorted(kinds)[-2] == 2:
        return 2
    if sorted(kinds)[-1] == 2:
        return 1
    return 0


def strength_joker(hand):
    kinds = collections.Counter(hand).values()
    jokers = collections.Counter(hand)["J"]
    if jokers >= 4:
        return 6
    if jokers == 3:
        if sorted(kinds)[-2] == 2:
            return 6
        else:
            return 5
    if jokers == 2:
        if max(kinds) == 3:
            return 6
        if sorted(kinds)[-2] == 2:
            return 5
        return 3
    if jokers == 1:
        if max(kinds) == 4:
            return 6
        if max(kinds) == 3:
            return 5
        if sorted(kinds)[-2] == 2:
            return 4
        if sorted(kinds)[-1] == 2:
            return 3
        return 1
    return strength(hand)


def rank_cards(x, y):
    if no_jokers:
        if strength(x[0]) < strength(y[0]):
            return -1
        if strength(x[0]) > strength(y[0]):
            return 1
        remapping = str.maketrans("AKQJT", "ZYXWV")
    else:
        if strength_joker(x[0]) < strength_joker(y[0]):
            return -1
        if strength_joker(x[0]) > strength_joker(y[0]):
            return 1
        remapping = str.maketrans("AKQJT", "ZYX1V")
    for a, b in zip(x[0].translate(remapping), y[0].translate(remapping)):
        if a != b:
            return -1 if ord(a) < ord(b) else 1
    return 0


hands = [hand.split() for hand in hands]
no_jokers = True
hands = sorted(hands, key=functools.cmp_to_key(rank_cards))
print("answer 1:", sum(int(bid) * (i + 1) for i, (hand, bid) in enumerate(hands)))

no_jokers = False
hands = sorted(hands, key=functools.cmp_to_key(rank_cards))
print("answer 2:", sum(int(bid) * (i + 1) for i, (hand, bid) in enumerate(hands)))
