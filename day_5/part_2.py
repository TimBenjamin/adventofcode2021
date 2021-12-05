
coords = set()
seenCoords = set()
multiples = 0

def run(filename):
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            cfrom, cto = line.split(" -> ")
            x1, y1 = cfrom.split(",")
            x2, y2 = cto.split(",")
            y1 = int(y1)
            y2 = int(y2)
            x1 = int(x1)
            x2 = int(x2)
            x_coords = []
            y_coords = []
            stuff_x = False
            stuff_y = False
            if y1 > y2:
                for i in range(y1, y2-1, -1):
                    y_coords.append(i)
            elif y2 > y1:
                for i in range(y1, y2+1):
                    y_coords.append(i)
            else:
                # need to add many of the same value
                stuff_y = True
            
            if x1 > x2:
                for i in range(x1, x2-1, -1):
                    x_coords.append(i)
            elif x2 > x1:
                for i in range(x1, x2+1):
                    x_coords.append(i)
            else:
                # add many
                stuff_x = True
            
            if stuff_y:
                for i in range(len(x_coords)):
                    y_coords.append(y1)
            elif stuff_x:
                for i in range(len(y_coords)):
                    x_coords.append(x1)
            
            for i in range(len(x_coords)):
                doCoord(str(x_coords[i]) + "," + str(y_coords[i]))

def doCoord(coord):
    global multiples
    global coords
    if coord in coords:
        if coord not in seenCoords:
            multiples += 1
            seenCoords.add(coord)
    else:
        coords.add(coord)


run("input.txt")
print(multiples)