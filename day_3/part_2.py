oxygen = []
scrubber = []
filename = "input.txt"
with open(filename) as file:
    while (line := file.readline().rstrip()):
        oxygen.append(line)
        scrubber.append(line)

def get_tallies(lines):
    tally_0 = []
    tally_1 = []
    for line in lines:
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
    return tally_0, tally_1      

def get_new_oxygen(oxygen, pos):
    tally_0, tally_1 = get_tallies(oxygen)
    most = "1"
    if tally_0[pos] > tally_1[pos]:
        most = "0" # ties are counted as 1
    new_oxygen = []
    for line in oxygen:
        bits = list(line)
        b = bits[pos]
        if b == most:
            new_oxygen.append(line)
    return new_oxygen

def get_new_scrubber(scrubber, pos):
    tally_0, tally_1 = get_tallies(scrubber)
    least = "0"
    if tally_1[pos] < tally_0[pos]:
        least = "1" # ties are counted as 0
    new_scrubber = []
    for line in scrubber:
        bits = list(line)
        b = bits[pos]
        if b == least:
            new_scrubber.append(line)
    return new_scrubber

def arse(foo):
    return int("".join(str(b) for b in foo), 2)

curpos = 0
for curpos in range(len(oxygen[0])):
    new_oxygen = get_new_oxygen(oxygen, curpos)
    if len(new_oxygen) > 1:
        oxygen = new_oxygen
    else:
        break
    
for curpos in range(len(scrubber[0])):
    new_scrubber = get_new_scrubber(scrubber, curpos)
    if len(new_scrubber) > 1:
        scrubber = new_scrubber
    else:
        break

solution = arse(new_oxygen) * arse(new_scrubber)
print(solution)