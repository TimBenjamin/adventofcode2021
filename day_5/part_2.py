


def run(filename):
    coords = {}
    multiples = 0
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
                coord = str(x_coords[i]) + "," + str(y_coords[i])
                coords[coord] = coords.get(coord, 0) + 1
                if coords[coord] == 2:
                    multiples += 1
    
    return multiples

multiples = run("input.txt")
print(multiples)