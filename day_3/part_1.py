
gamma = []
epsilon = []
tally_0 = []
tally_1 = []

with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        bits = list(line)
        for i, b in list(enumerate(bits)):
            if len(tally_1) < i+1:
                tally_0.append(0)
                tally_1.append(0)
            if b == "1":
                tally_0[i] += 0
                tally_1[i] += 1
            else:
                tally_0[i] += 1
                tally_1[i] += 0

for i in range(len(tally_0)):
    if tally_1[i] > tally_0[i]:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

def arse(foo):
    return int("".join(str(b) for b in foo), 2)

gamma = arse(gamma)
epsilon = arse(epsilon)
solution = gamma * epsilon
print(solution)
