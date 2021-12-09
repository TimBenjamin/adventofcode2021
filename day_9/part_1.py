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
            minima.append(point)

print(sum(minima) + len(minima))