def getInput(filename):
    with open(filename) as file:
        line = file.readline().rstrip()
    population = line.split(",")
    fish = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }
    for p in population:
        fish[int(p)] += 1
    return fish

fish = getInput("input.txt")
    
for day in range(256):
    numNew = fish[0]
    for f in range(1, 9):
        fish[f-1] = fish[f]
    fish[8] = numNew
    fish[6] += numNew

total = 0
for f in range(9):
    total += fish[f]

print(total)
