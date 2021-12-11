import statistics

navigation_syntax = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]
navigation_syntax = open("inputs/day10.txt").read().splitlines()

illegal_characters = []
incomplete_lines = []
for line in navigation_syntax:
    syntax_checker = []
    for symbol in line:
        if symbol in "([{<":
            syntax_checker.append(symbol)
        else:
            if syntax_checker[-1] == symbol.translate(symbol.maketrans(")]}>", "([{<")):
                syntax_checker.pop()
            else:
                illegal_characters.append(symbol)
                break
    else:
        incomplete_lines.append(syntax_checker)

syntax_error_score = illegal_characters.count(")") * 3 + illegal_characters.count("]") * 57
syntax_error_score += + illegal_characters.count("}") * 1197 + illegal_characters.count(">") * 25137
print("answer 1:", syntax_error_score)

autocomplete_scores = []
for incomplete_line in incomplete_lines:
    autocomplete_score = 0
    for symbol in reversed(incomplete_line):
        autocomplete_score *= 5
        autocomplete_score += {"(": 1, "[": 2, "{": 3, "<": 4}[symbol]
    autocomplete_scores.append(autocomplete_score)
print("answer 2:", statistics.median(autocomplete_scores))
