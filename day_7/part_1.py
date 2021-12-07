
from statistics import median

with open("input.txt") as file:
    crabstrings = file.readline().rstrip().split(",")
    crabs = []
    max = 0
    min = 1000000
    for i in crabstrings:
        crab = int(i)
        crabs.append(crab)
        if crab > max:
            max = crab
        if crab < min:
            min = crab

def calculateFuel(crabs, pos):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - pos)
    return fuel

pos = int(median(crabs))
fuel = calculateFuel(crabs, pos)

while True:
    pos += 1
    if pos > max:
        break
    f = calculateFuel(crabs, pos)
    if f < fuel:
        fuel = f
    if f > fuel:
        break

while True:
    pos -= 1
    if pos < min:
        break
    f = calculateFuel(crabs, pos)
    if f < fuel:
        fuel = f
    if f > fuel:
        break

print(fuel)