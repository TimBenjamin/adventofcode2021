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
        newDots.add(newDot)
    dots = newDots.copy()

# visualise the dots
max_x = 0
max_y = 0
for dot in dots:
    if dot[0] > max_x:
        max_x = dot[0]
    if dot[1] > max_y:
        max_y = dot[1]

row = [" "] * (max_x+1)
output = []
for _ in range(max_y+1):
    output.append(row.copy())

for dot in dots:
    x = dot[0]
    y = dot[1]
    output[y][x] = "#"

for row in output:
    print("".join(row))

