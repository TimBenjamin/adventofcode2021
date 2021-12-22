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

# for each range, get the total number of points in the range => N
# if state == "on", add N to "on"
# need to subtract off states from on states

def removeRangeFromSteps(step, steps):
    # we are removing 1's points from 2's points
    x1_from = step["ranges"][0][0]
    x1_to = step["ranges"][0][1]
    y1_from = step["ranges"][1][0]
    y1_to = step["ranges"][1][1]
    z1_from = step["ranges"][2][0]
    z1_to = step["ranges"][2][1]
    newSteps = []
    for i, s in enumerate(steps):
        x2_from = s["ranges"][0][0]
        x2_to = s["ranges"][0][1]
        y2_from = s["ranges"][1][0]
        y2_to = s["ranges"][1][1]
        z2_from = s["ranges"][2][0]
        z2_to = s["ranges"][2][1]
        # check if 2 is entirely inside 1, which destroys 2
        if x1_from <= x2_from and x1_to >= x2_to and y1_from <= y2_from and y1_to >= y2_to and z1_from <= z2_from and z1_to >= z2_to:
            # the 1 range completely encompasses the 2 range
            # we can remove the 2 range - i.e. ignore it here
            # (do not add it to newSteps)
            pass
        # check if there is any overlap (or if 1 is entirely inside 2), if so, we need to make some new cuboids out of 2
        # (and remove 2)
        elif x1_from <= x2_from or x1_to >= x2_to:
    return newSteps


def oldremoveRangeFromSteps(step, steps):
    # for each one of steps, need to nibble out any bit of step that overlaps it
    x1_from = step["ranges"][0][0]
    x1_to = step["ranges"][0][1]
    y1_from = step["ranges"][1][0]
    y1_to = step["ranges"][1][1]
    z1_from = step["ranges"][2][0]
    z1_to = step["ranges"][2][1]
    newSteps = []
    for i, s in enumerate(steps):
        x2_from = s["ranges"][0][0]
        x2_to = s["ranges"][0][1]
        y2_from = s["ranges"][1][0]
        y2_to = s["ranges"][1][1]
        z2_from = s["ranges"][2][0]
        z2_to = s["ranges"][2][1]
        if x1_from <= x2_from and x1_to >= x2_to and y1_from <= y2_from and y1_to >= y2_to and z1_from <= z2_from and z1_to >= z2_to:
            # the 1 range completely encompasses the 2 range
            # we can remove the 2 range - i.e. ignore it here
            # (do not add it to newSteps)
            pass
        elif x1_to > x2_from and x1_from <= x2_from and y1_to > y2_from and y1_from <= y2_from and z1_to > z2_from and z1_from <= z2_from: # etc
            # the 1 range starts outside the 2 range, but ends inside it
            # reduce the 2 range TODO
            # add the reduced 2 range to newSteps
            newSteps.append({
                "state": "on",
                "ranges": [(x2_from,x2_to), (y2_from, y2_to), (z2_from, z2_to)]
            })
        elif x1_from < x2_to and x1_to >= x2_to: #etc
            # the 1 range ends outside the 2 range, but starts inside it
            # reduce the 2 range TODO
            # add the reduced 2 range to newSteps
            newSteps.append({
                "state": "on",
                "ranges": [(x2_from,x2_to), (y2_from, y2_to), (z2_from, z2_to)]
            })
            pass
        elif x1_from > x2_from and x1_to < x2_to: #etc
            # the 1 range is entirely inside the 2 range
            # need to split the 2 range into SIX new steps
            # TODO
            # x2_from : x1_from
            # x1_to : x2_to
            # add the two new ranges
            # do not add the old 2 range!
            newSteps.append({
                "state": "on",
                "ranges": [(x2_from,x1_from), (y2_from, y1_from), (z2_from, z2_from)]
            })
            newSteps.append({
                "state": "on",
                "ranges": [(x1_to,x2_to), (y1_to, y2_to), (z1_to, z2_to)]
            })
            
    # at the end, we have removed the off step from all the on steps,
    # so everything left in the off step is irrelevant and can be discarded...
    return newSteps


def addRangeToSteps(step, steps):
    # need to reduce step's coords to remove any that have already been added in previous steps
    # if there's anything left, append it to steps
    # TODO: could expand the 2 range instead of reducing the 1 range but I think it's the same difference
    x1_from = step["ranges"][0][0]
    x1_to = step["ranges"][0][1]
    y1_from = step["ranges"][1][0]
    y1_to = step["ranges"][1][1]
    z1_from = step["ranges"][2][0]
    z1_to = step["ranges"][2][1]
    print("1 range:", x1_from, x1_to, y1_from, y1_to, z1_from, z1_to)
    for s in steps:
        x2_from = s["ranges"][0][0]
        x2_to = s["ranges"][0][1]
        y2_from = s["ranges"][1][0]
        y2_to = s["ranges"][1][1]
        z2_from = s["ranges"][2][0]
        z2_to = s["ranges"][2][1]
        if x1_from >= x2_from and x1_to <= x2_to and y1_from >= y2_from and y1_to <= y2_to and z1_from >= z2_to and z1_to <= z2_to:
            # the 1 range is entirely inside the 2 range
            # so we don't need to add it at all
            print("the 1 range is entirely inside a 2 range, skip it")
            return steps
        if x1_from >= x2_from and x1_from <= x2_to and y1_from >= y2_from and y1_from <= y2_to and z1_from >= z2_from and z1_from <= z2_to:
            # the 1 range starts inside the 2 range
            # shrink the 1 range so that it ends before the 2 range
            print("the 1 range starts inside the 2 range, shrink the 1 range")
            if x1_to >= x2_to:
                x1_from = x2_to
            if y1_to >= y2_to:
                y1_from = y2_to
            if z1_to >= z2_to:
                z1_from = z2_to
        if x1_to >= x2_from and x1_to <= x2_to and y1_to >= y2_from and y1_to <= y2_to and z1_to >= z2_from and z1_to <= z2_to:
            # the 1 range ends inside the 2 range
            print("the 1 range ends inside the 2 range, shrink the 1 range")
            if x1_from >= x2_from:
                x1_to = x2_from
            if y1_from >= y2_from:
                y1_to = y2_from
            if y1_from >= y2_from:
                y1_to = y2_from
        if x1_from == x1_to and y1_from == y1_to and z1_from == z2_to:
            # the 1 range has shrunk to nothing
            # no need to add it
            return steps

    # having reduced it as above, is there anything left?
    if x1_from == x1_to and y1_from == y1_to and z1_from == z2_to:
        # the 1 range has shrunk to nothing
        # no need to add it
        print("after all, we reduced the 1 to nothing")
        return steps
    else:
        print("after all, there is something left, add it")
        steps.append({
            "state": "on",
            "ranges": [(x1_from,x1_to), (y1_from, y1_to), (z1_from, z1_to)]
        })
    return steps

# go through the steps
# combine all the on steps as we find them
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

