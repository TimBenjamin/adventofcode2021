
coords = {}
multiples = 0

def run(filename):
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            cfrom, cto = line.split(" -> ")
            x1, y1 = cfrom.split(",")
            x2, y2 = cto.split(",")
            if x1 == x2:
                y1 = int(y1)
                y2 = int(y2)
                if y1 > y2:
                    for i in range(y1, y2-1, -1):
                        doCoord(x1 + "," + str(i))
                else:
                    for i in range(y1, y2+1):
                        doCoord(x1 + "," + str(i))
            elif y1 == y2:
                x1 = int(x1)
                x2 = int(x2)
                if x1 > x2:
                    for i in range(x1, x2-1, -1):
                        doCoord(str(i) + "," + y1)
                else:
                    for i in range(x1, x2+1):
                        doCoord(str(i) + "," + y1)
            else:
                # ignore diagonals
                continue

def doCoord(coord):
    global multiples
    global coords
    if coord in coords:
        coords[coord] += 1
        if coords[coord] == 2:
            multiples += 1
    else:
        coords[coord] = 1
    

run("input.txt")
print(multiples)