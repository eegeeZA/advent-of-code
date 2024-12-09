try:
    disk_map = open("inputs/day09.txt").read()
except FileNotFoundError:
    disk_map = """
2333133121414131402
"""[1:]
disk_map = disk_map.strip()

files = [int(bit) for bit in disk_map[::2]]
space = [int(bit) for bit in disk_map[1::2]]
checksum = 0
file_id = 0
last_file_id = len(files) - 1
i = 0
while files:
    for _ in range(files.pop(0)):
        checksum += i * file_id
        i += 1
    file_id += 1
    for _ in range(space.pop(0)):
        if not files:
            break
        if not files[-1]:
            files.pop()
            last_file_id -= 1
        checksum += i * last_file_id
        i += 1
        files[-1] -= 1
print("answer 1:", checksum)

files = {i: int(bit) for i, bit in enumerate(disk_map[::2])}
space = {i: int(bit) for i, bit in enumerate(disk_map[1::2])}
space_remaining = {i: int(bit) for i, bit in enumerate(disk_map[1::2])}
new_map = {}
for file_id in reversed(files):
    for i in range(file_id):
        if files[file_id] <= space_remaining[i]:
            offset = sum(size for check_id, size in files.items() if check_id <= i)
            offset += sum(size for check_id, size in space.items() if check_id < i)
            if space_remaining[i] != space[i]:
                offset += space[i] - space_remaining[i]
            space_remaining[i] -= files[file_id]
            space[file_id - 1] += files[file_id]
            space_remaining[file_id - 1] += files[file_id]
            for x in range(offset, offset + files[file_id]):
                new_map[x] = file_id
            files[file_id] = 0
            break
checksum = 0
i = 0
for file_id in files:
    for x in range(files[file_id]):
        new_map[i] = file_id
        i += 1
    if file_id in space:
        i += space[file_id]
for i in range(sum(int(x) for x in disk_map)):
    if i in new_map:
        checksum += i * new_map[i]
print("answer 2:", checksum)
