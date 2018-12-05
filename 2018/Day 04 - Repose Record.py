import re
from collections import Counter

entries = sorted(open("inputs/day04.txt").readlines())
sleep_records = {}
guard = start = None
for entry in entries:
    if "begins shift" in entry:
        guard = int(re.search("#(\d+)", entry).group(1))
        if guard not in sleep_records:
            sleep_records[guard] = []
    if "falls asleep" in entry:
        start = int(re.search(":(\d+)", entry).group(1))
    if "wakes up" in entry:
        end = int(re.search(":(\d+)", entry).group(1))
        for minute in range(start, end):
            sleep_records[guard].append(minute)

sleepy_guard = None
most_asleep = 0
for guard, sleeps in sleep_records.items():
    if len(sleeps) > most_asleep:
        most_asleep = len(sleeps)
        sleepy_guard = guard
common_minute = Counter(sleep_records[sleepy_guard]).most_common(1)[0][0]
print("answer 1:", sleepy_guard * common_minute)

sleepy_guard = None
sleepy_minute = None
most_asleep = 0
for guard, sleeps in sleep_records.items():
    if not sleep_records[guard]:
        continue
    minute, count = Counter(sleep_records[guard]).most_common(1)[0]
    if count > most_asleep:
        most_asleep = count
        sleepy_guard = guard
        sleepy_minute = minute
print("answer 2:", sleepy_guard * sleepy_minute)
