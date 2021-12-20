import sys


# I'd like each scanner in a list of scanners
scanners = list()
# within each element, a list of rotations
# within each rotation, a set of tuples for the points

def rotateAroundX(t):
    x = t[0]
    y = t[1]
    z = t[2]
    return tuple((x, -z, y))

def rotateAroundY(t):
    x = t[0]
    y = t[1]
    z = t[2]
    return tuple((-z, y, x))

def rotateAroundZ(t):
    x = t[0]
    y = t[1]
    z = t[2]
    return tuple((y, -x, z))

def addRotations(rotations):
    # rotations[0] is a list of each (x,y,z)
    # I want to rotate each (x,y,z) into rotations[1], rotations[2], etc
    
    # .{ .x = self.x, .y = self.y, .z = self.z }, // x -> +x
    # .{ .x = -self.x, .y = self.y, .z = -self.z }, // x -> -x
    # .{ .x = -self.y, .y = self.x, .z = self.z }, // x -> +y
    # .{ .x = self.y, .y = -self.x, .z = self.z }, // x -> -y
    # .{ .x = -self.z, .y = self.y, .z = self.x }, // x -> z
    # .{ .x = self.z, .y = self.y, .z = -self.x }, // x -> -z
    for (x,y,z) in rotations[0]:
        for i in range(1, 4):
            rotations[i].append(rotateAroundX((x,y,z)))
        rotations[4].append((-x, y, -z))
        for i in range(5, 8):
            rotations[i].append(rotateAroundX((-x, y, -z)))
        rotations[8].append((-y, x, z))
        for i in range(9, 12):
            rotations[i].append(rotateAroundY((-y, x, z)))
        rotations[12].append((y, -x, z))
        for i in range(13, 16):
            rotations[i].append(rotateAroundY((y, -x, z)))
        rotations[16].append((-z, y, x))
        for i in range(17, 20):
            rotations[i].append(rotateAroundZ((-z, y, x)))
        rotations[20].append((z, y, -x))
        for i in range(21, 24):
            rotations[i].append(rotateAroundZ((z, y, -x)))
    # rotations[1].append((-x,y,z))
    # rotations[2].append((x,-y,z))
    # rotations[3].append((x,y,-z))
    # rotations[4].append((-x,-y,z))
    # rotations[5].append((-x,y,-z))
    # rotations[6].append((x,-y,-z))
    # rotations[7].append((-x,-y,-z))
    # rotations[8].append((x,z,y))
    # rotations[9].append((-x,z,y))
    # rotations[10].append((x,-z,y))
    # rotations[11].append((x,z,-y))
    # rotations[12].append((-x,-z,y))
    # rotations[13].append((-x,z,-y))
    # rotations[14].append((x,-z,-y))
    # rotations[15].append((-x,-z,-y))
    # rotations[16].append((y,x,z))
    # rotations[17].append((-y,x,z))
    # rotations[18].append((y,-x,z))
    # rotations[19].append((y,x,-z))
    # rotations[20].append((-z,-x,y))
    # rotations[21].append((-z,x,-y))
    # rotations[22].append((z,-x,-y))
    # rotations[23].append((-z,-x,-y))

    return rotations

while line := sys.stdin.readline():
    line = line.strip()
    if "scanner" in line:
        # empty the container
        rotations = []
        for i in range(0,24):
            rotations.append([])
    elif len(line) == 0:
        # make the 23 other rotations
        rotations = addRotations(rotations)
        # store the container
        scanners.append(rotations)
        pass
    else:
        # add the line to the first rotation
        rotations[0].append(tuple(map(lambda x: int(x),line.split(","))))
    #print(line)
# make the 23 other rotations last time
for (x,y,z) in rotations[0]:
    rotations = addRotations(rotations)
# store the last container
scanners.append(rotations)

# try:
# set1 = [(-1,-1),(-5,0),(-2,1)]
# set0 = [(4,1),(0,2),(3,3)]

# p0 = set0[0]
# print("p0:", p0)

# for p1 in set1:
#     print("-------------")
#     print("p1:", p1)
#     # take p1 from p0
#     modifier = (p0[0]-p1[0], p0[1]-p1[1])
#     #print("modifier:", modifier)
#     for p in set1:
#         test = (modifier[0] + p[0], modifier[1] + p[1])
#         if test in set0:
#             print("found:", test)

# set0 = scanners[0][0] # first rotation of first scanner, compare everything to this
# p0 = set0[0] # first point of the origin scanner
# rotation = 0
# scanner = 1
# for set1 in scanners[scanner]:
#     for p1 in set1:
#         # take p1 from p0
#         modifier = (p0[0]-p1[0], p0[1]-p1[1], p0[2]-p1[2])
#         matches = []
#         for p in set1:
#             test = (modifier[0] + p[0], modifier[1] + p[1], modifier[2] + p[2])
#             if test in set0:
#                 matches.append(test)
#         if len(matches) >= 12:
#             print("found a good one!")
#             print("rotation: ", rotation)
#             print("position of scanner "+str(scanner)+" relative to 0:", modifier)
#             for m in matches:
#                 print(m)
#     rotation += 1

# now compare the others, not 0, to 1
# 5 was the good rotation for scanner 1, found above
# scanner 1 is at (68, -1246, -43)
lastScanner = 1
lastRotation = 5
originPoints = scanners[lastScanner][lastRotation] # compare everything to this
for origin in originPoints:
    #origin = originPoints[0] # first point of the origin scanner
    for scanner in range(0,5):
        if scanner == lastScanner: continue
        print("-- SCANNER " + str(scanner) + " --")
        rotation = 0
        for rotationSet in scanners[scanner]:
            for point in rotationSet: 
                # take p1 from p0
                modifier = (origin[0]-point[0], origin[1]-point[1], origin[2]-point[2])
                matches = []
                for p in rotationSet:
                    test = (modifier[0] + p[0], modifier[1] + p[1], modifier[2] + p[2])
                    if test in originPoints:
                        matches.append(test)
                if len(matches) >= 12:
                    print("found a good one!")
                    print("rotation: ", rotation)
                    print("position of scanner "+str(scanner)+" relative to "+str(lastScanner)+":", modifier)
                    print("overlapping points:")
                    for m in matches:
                        print(m)
            rotation += 1