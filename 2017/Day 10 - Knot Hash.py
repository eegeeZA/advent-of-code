lengths = [230, 1, 2, 221, 97, 252, 168, 169, 57, 99, 0, 254, 181, 255, 235, 167]
hash_list = [_ for _ in range(256)]
i = 0
skip = 0
for length in lengths:
    sub_hash = []
    for j in range(i, i + length):
        sub_hash.append(hash_list[j % len(hash_list)])
    for j in range(i, i + length):
        hash_list[j % len(hash_list)] = sub_hash.pop()
    i += length + skip
    skip += 1
print("answer 1:", hash_list[0] * hash_list[1])


def knot_hash(input_string):
    lengths = []
    for length in input_string:
        for char in str(length):
            lengths.append(ord(char))
    lengths += [17, 31, 73, 47, 23]
    hash_list = [_ for _ in range(256)]
    i = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            sub_hash = []
            for j in range(i, i + length):
                sub_hash.append(hash_list[j % len(hash_list)])
            for j in range(i, i + length):
                hash_list[j % len(hash_list)] = sub_hash.pop()
            i += length + skip
            skip += 1
    dense_list = []
    for i in range(16):
        dense = hash_list[i * 16]
        for j in range(i * 16 + 1, i * 16 + 16):
            dense ^= hash_list[j]
        dense_list.append(dense)
    new_hash = ""
    for dense in dense_list:
        new_hash += '{:02x}'.format(dense)
    return new_hash


print("answer 2:", knot_hash("230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167"))
