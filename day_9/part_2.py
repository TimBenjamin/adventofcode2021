heightmap = []
with open("input.txt") as file:
    while line := file.readline().rstrip():
        heights = list(map(int, list(line)))
        heightmap.append(heights)

def getAdjacent(heightmap, i, j):
    adjacents = []
    if j > 0:
        adjacents.append(heightmap[i][j-1])
    if j < len(heightmap[i])-1:
        adjacents.append(heightmap[i][j+1])
    if i > 0:
        adjacents.append(heightmap[i-1][j])
    if i < len(heightmap)-1:
        adjacents.append(heightmap[i+1][j])
    return adjacents

minima = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        point = heightmap[i][j]
        if point == 9:
            continue
        adjacents = getAdjacent(heightmap, i, j)
        local_min = True
        for a in adjacents:
            if a <= point:
                local_min = False
                break
        if local_min:
            minima.append([i,j,point])

def getAdjacentPoints(heightmap, i, j):
    adjacents = []
    if j > 0:
        if heightmap[i][j-1] < 9:
            adjacents.append([i,j-1])
    if j < len(heightmap[i])-1:
        if heightmap[i][j+1] < 9:
            adjacents.append([i,j+1])
    if i > 0:
        if heightmap[i-1][j] < 9:
            adjacents.append([i-1,j])
    if i < len(heightmap)-1:
        if heightmap[i+1][j] < 9:
            adjacents.append([i+1,j])
    return adjacents

def fillBasin(heightmap, basin):
    new_basin = basin.copy()
    for p in basin:
        adjacents = getAdjacentPoints(heightmap, p[0], p[1])
        for a in adjacents:
            new_basin.add(tuple(a))
    basin = new_basin.copy()
    return basin

def getBasin(heightmap, i, j):
    basin = set()
    basin.add(tuple([i,j]))
    # I need all contiguous points that are not 9
    # do this row first:
    for k in range(j-1, -1, -1):
        if heightmap[i][k] < 9:
            basin.add(tuple([i,k]))
        else: break
    for k in range(j+1, len(heightmap[i])-1):
        if heightmap[i][k] < 9:
            basin.add(tuple([i,k]))
        else: break
    # we want to recursively get the adjacents for all of these points, that aren't 9
    while True:
        new_basin = fillBasin(heightmap, basin)
        if len(new_basin) == len(basin):
            break
        basin = new_basin.copy()
    return basin

basinSizes = []
for i, j, point in minima:
    basin = getBasin(heightmap, i, j)
    basinSizes.append(len(basin))

revSort = sorted(basinSizes)[::-1]
print(revSort[0] * revSort[1] * revSort[2])
