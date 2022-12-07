import collections

filesystem = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
filesystem = open("inputs/day07.txt").read()

directories = collections.defaultdict(int)
visited = []
for line in filesystem.split("\n$ "):
    if line.startswith("$ cd") or line.startswith("cd"):
        if ".." in line:
            visited.pop()
        else:
            visited.append(line.split()[-1])
    elif line.startswith("ls"):
        for path in line.splitlines()[1:]:
            if not path.startswith("dir"):
                for i in range(len(visited)):
                    directories[tuple(visited[:i + 1])] += int(path.split()[0])

total = 0
candidates = []
for size in directories.values():
    if size <= 100_000:
        total += size
    if (70_000_000 - directories[tuple("/")]) + size > 30_000_000:
        candidates.append(size)

print("answer 1:", total)
print("answer 2:", min(candidates))
