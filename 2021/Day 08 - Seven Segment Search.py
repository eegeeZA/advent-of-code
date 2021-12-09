signal_patterns = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]
signal_patterns = open("inputs/day08.txt").readlines()

unique_segments = 0
for signal_pattern in signal_patterns:
    _, outputs = signal_pattern.split("|")
    output_lengths = list(map(len, outputs.split()))
    unique_segments += output_lengths.count(2)
    unique_segments += output_lengths.count(3)
    unique_segments += output_lengths.count(4)
    unique_segments += output_lengths.count(7)
print("answer 1:", unique_segments)

output_total = 0
for signal_pattern in signal_patterns:
    inputs, outputs = signal_pattern.split("|")
    input_values = list(map(lambda x: set(x), sorted(inputs.split(), key=len)))
    output_values = list(map(lambda x: set(x), outputs.split()))

    combos = [set()] * 10
    combos[1] = input_values[0]
    combos[7] = input_values[1]
    combos[4] = input_values[2]
    combos[8] = input_values[-1]

    for value in input_values[3:6]:
        if combos[1] <= value:
            combos[3] = value
        elif (combos[4] - combos[1]) <= value:
            combos[5] = value
        else:
            combos[2] = value

    for value in input_values[6:9]:
        if (combos[5] | combos[1]) == value:
            combos[9] = value
        elif (combos[2] - combos[1] | combos[5]) == value:
            combos[6] = value
        else:
            combos[0] = value

    output_total += combos.index(output_values[0]) * 1000
    output_total += combos.index(output_values[1]) * 100
    output_total += combos.index(output_values[2]) * 10
    output_total += combos.index(output_values[3])
print("answer 2:", output_total)
