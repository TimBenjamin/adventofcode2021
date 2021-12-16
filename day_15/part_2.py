from datetime import date, datetime

small = []
levels = []
with open("input.txt") as file:
    while line := file.readline().strip():
        line_str = list(line)
        nums = list(map(int, line_str))
        # expand it horizontally to 5x as large:
        row = nums.copy()
        for i in range(4):
            for n in nums:
                f = (n + i + 1)
                if f > 9:
                    f = f - 9
                row.append(f)
        small.append(row)

# expand it vertically to 5x as large:
levels = small.copy()
for i in range(4):
    for row in small:
        newRow = []
        for n in row:
            f = (n + i + 1)
            if f > 9:
                f = f - 9
            newRow.append(f)
        levels.append(newRow)

# points gives me the neighbours of any given point, and the distance from source (0,0) to that point
points = {}
delta = [(-1,0), (0,-1), (1, 0), (0, 1)]
for i in range(len(levels)):
    for j in range(len(levels[i])):
        t = (i,j)
        opts = []
        for d in delta:
            if i+d[0] >= 0 and i+d[0] < len(levels) and j+d[1] >= 0 and j+d[1] < len(levels[i]):
                opts.append((i+d[0], j+d[1]))
        distance = 0
        points[t] = {
            "neighbours": opts, 
            "distance": None,
            "in_sptset": False, # instead of an actual set, this might be slightly faster
        }

source = (0,0)
dest = (len(levels)-1,len(levels[0])-1)

# 1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in the shortest-path tree, i.e., whose minimum distance from the source is calculated and finalized. Initially, this set is empty. 
# sptset = set()
# moved into points

# 2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first. 
points[source]["distance"] = 0

# 3) While sptSet doesn’t include all vertices 
# ….a) Pick a vertex u which is not there in sptSet and has a minimum distance value. 
# ….b) Include u to sptSet. 
# ….c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if the sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v. 
pointsWithDistance = {}
pointsWithDistance[source] = points[source]
while True: # break out when we add 
    # a)
    m = 100000000
    selectedPoint = None
    for p in pointsWithDistance:
        if points[p]["in_sptset"] is False and points[p]["distance"] < m:
            selectedPoint = p
            m = points[p]["distance"]

    if selectedPoint is not None:
        p = selectedPoint
        # b)
        #sptset.add(p)
        points[p]["in_sptset"] = True
        # this point is no longer needed in pointsWithDistance
        del pointsWithDistance[p]
        # c)
        # To update the distance values, iterate through all adjacent vertices. 
        for adj in points[p]["neighbours"]:
            # For every adjacent vertex v, if the sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v. 
            u_dist = points[p]["distance"]
            uv_edge_weight = levels[adj[0]][adj[1]]
            if points[adj]["distance"] is None or u_dist + uv_edge_weight < points[adj]["distance"]:
                points[adj]["distance"] = levels[adj[0]][adj[1]] + points[p]["distance"]
                pointsWithDistance[adj] = points[adj]
    else:
        # 3) While sptSet doesn’t include all vertices 
        # nothing left to add
        break
    
print(points[dest]["distance"])