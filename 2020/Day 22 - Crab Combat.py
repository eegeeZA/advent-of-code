def recursive_combat(player1, player2, play_recursive):
    player1, player2 = player1.copy(), player2.copy()
    player1_seen, player2_seen = [], []
    while player1 and player2:
        if play_recursive:
            if player1 in player1_seen or player2 in player2_seen:
                return True, player1
            player1_seen.append(player1.copy())
            player2_seen.append(player2.copy())

        a, b = player1.pop(0), player2.pop(0)
        if play_recursive and len(player1) >= a and len(player2) >= b:
            player1_won, _ = recursive_combat(player1[:a], player2[:b], play_recursive)
        else:
            player1_won = a > b

        if player1_won:
            player1.extend([a, b])
        else:
            player2.extend([b, a])
    return (True, player1) if player1 else (False, player2)


players = []
for player in open("inputs/day22.txt").read().split("\n\n"):
    players.append([int(card) for card in player.rstrip().split("\n")[1:]])
_, winning_cards = recursive_combat(*players, False)
print("answer 1:", sum([(i + 1) * card for i, card in enumerate(reversed(winning_cards))]))
_, winning_cards = recursive_combat(*players, True)
print("answer 2:", sum([(i + 1) * card for i, card in enumerate(reversed(winning_cards))]))
