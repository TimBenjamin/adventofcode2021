dots = set()
folds = []
with open("input.txt") as file:
    while line := file.readline().strip():
        dots.add(tuple(map(lambda x: int(x),line.split(","))))
    # now we have a blank line
    # now we have the fold instructions
    while line := file.readline().strip():
        fold = line[11:].split("=")
        fold[1] = int(fold[1])
        folds.append(fold)

# part 1 is concerned only with the first fold - break after first iteration
for fold in folds:
    axis = fold[0]
    v = fold[1]
    
    # NB the fold-line itself disappears too
    newDots = set()
    for dot in dots:
        if axis == "y":
            if dot[1] > v:
                d = v - (dot[1] - v)
                newDot = (dot[0], d)
                newDots.add(newDot)
            elif dot[1] < v:
                newDot = dot
        elif axis == "x":
            if dot[0] > v:
                d = v - (dot[0] - v)
                newDot = (d, dot[1])
                newDots.add(newDot)
            elif dot[0] < v:
                newDot = dot
        #print(str(dot) + " folds to " + str(newDot))
        newDots.add(newDot)
        # as it's a set, it should automatically "overlap" the dots when we add()
    dots = newDots.copy()
    break

print(len(dots))
