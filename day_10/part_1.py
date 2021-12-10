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

corrupt_lines = []
for line in lines:
    while True:
        n = simplify(line)
        if len(n) == len(line):
            break
        line = n
    # an INCOMPLETE line now consists of only opening brackets
    openers_re = "[\(\[\{\<]+"
    closers_re = "[\)\]\}\>]+"
    x = re.search(closers_re, line)
    if x != None:
        corrupt_lines.append(line)

scorecard = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
score = 0
for c in corrupt_lines:
    # illegal characters are closers, so remove all openers:
    c = re.sub(openers_re, "", c)
    # we want the FIRST illegal character:
    score += scorecard[c[0]]
print(score)