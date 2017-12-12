passphrases = open("inputs/day04.txt").readlines()
valid_count = 0
for passphrase in passphrases:
    seen = []
    for piece in passphrase.split():
        if piece in seen:
            break
        seen.append(piece)
    else:
        valid_count += 1
print("answer 1:", valid_count)

valid_count = 0
for passphrase in passphrases:
    seen = []
    for piece in passphrase.split():
        if sorted(piece) in seen:
            break
        seen.append(sorted(piece))
    else:
        valid_count += 1
print("answer 2:", valid_count)
