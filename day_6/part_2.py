with open("input.txt") as file:
    population = file.readline().rstrip().split(",")
fish = [0] * 9
for p in population:
    fish[int(p)] += 1
for _ in range(256):
    numNew = fish[0]
    for f in range(1, 9):
        fish[f-1] = fish[f]
    fish[8] = numNew
    fish[6] += numNew
print(sum(fish))