
from statistics import mean
from math import ceil

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
        steps = abs(crab - pos)
        f = 1
        for i in range(steps):
            fuel += f
            f += 1
    return fuel

pos = ceil(mean(crabs))
fuel = calculateFuel(crabs, pos)

pos_a = pos_b = pos
while True:
    pos_a += 1
    pos_b -= 1
    if pos_a > max and pos_b < min:
        break
    if pos_a < max:
        f = calculateFuel(crabs, pos_a)
        if f < fuel:
            fuel = f
        if f > fuel:
            pos_a = max+1
    if pos_b > min:
        f = calculateFuel(crabs, pos_b)
        if f < fuel:
            fuel = f
        if f > fuel:
            pos_b = min-1
    
print(fuel)