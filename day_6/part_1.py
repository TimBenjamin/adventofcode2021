def getInput(filename):
    with open(filename) as file:
        line = file.readline().rstrip()
    fish_str = line.split(",")
    return map(int, fish_str)

fish = getInput("input.txt")
for day in range(80):
    newFish = []
    for f in fish:
        if f == 0:
            f = 6
            newFish.append(f)
            newFish.append(8)
        else:
            f -= 1
            newFish.append(f)
    fish = newFish

print(len(fish))


