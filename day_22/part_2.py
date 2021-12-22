import sys

steps = []
while line := sys.stdin.readline().strip():
    line = line.split(" ")
    state = line[0]
    xyz = line[1].split(",")
    
    ranges = []
    for i in range(3):
        s = xyz[i].split("=")[1].split("..")
        ranges.append((int(s[0]), int(s[1])))
    
    step = {
        "state": state,
        "ranges": ranges
    }

    steps.append(step)

on = 0

# go through the steps after the first one
# with the "on" steps:
#   if a step overlaps the previous step
#       create a negative cuboid the size of the overlap
# with the "off" steps:
#   if it overlaps a previous "on" cube
#       create a negative cuboid the size of the overlap
#   if it overlaps a previous negative/off cube - that means it's overlapping an overlap of two positive cubes
#       create a positive cube the size of the overlap, which counteracts << what?

# for an overlap to exist, x y and z all have to overlap


# when we find an off step, remove the off step ranges from the preceding on step ranges
# (and then discard the off step as it is no longer relevant)
# what is left can be added up

combinedSteps = []
for step in steps:
    if len(combinedSteps) > 0:
        if step["state"] == "on":
            print("attempt to combine")
            combinedSteps = addRangeToSteps(step, combinedSteps)
        else:
            print("attempt to remove an off range from all preceding combined on ranges")
            combinedSteps = removeRangeFromSteps(step, combinedSteps)
    else:
        combinedSteps.append(step)

for c in combinedSteps:
    print(c)

total = 0
# to get the grand total at the end,
# we can just make cuboids out of each set of coordinates
# total += (lenX * lenY * lenZ) 
print(total)

