import re

lines = []
with open("input.txt") as file:
    while line := file.readline().strip():
        lines.append(line)

def simplify(line):
    line = line.replace("()", "")
    line = line.replace("[]", "")
    line = line.replace("{}", "")
    line = line.replace("<>", "")
    return line

incomplete_lines = []
for line in lines:
    while True:
        n = simplify(line)
        if len(n) == len(line):
            break
        line = n
    # an INCOMPLETE line now consists of only opening brackets
    closers_re = "[\)\]\}\>]+"
    x = re.search(closers_re, line)
    if x == None:
        incomplete_lines.append(line)

scorecard = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
closers = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
scores = []
for i in incomplete_lines:
    line_score = 0
    while len(i) > 0:
        i += closers[i[-1:]]
        line_score *= 5
        line_score += scorecard[i[-1:]]
        i = i[:-2]
    scores.append(line_score)

print(sorted(scores)[int((len(scores)-1)/2)])