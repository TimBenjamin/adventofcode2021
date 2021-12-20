import sys


# I'd like each scanner in a list of scanners
scanners = list()
# within each element, a list of rotations
# within each rotation, a set of tuples for the points

def addRotations(rotations,x,y,z):
    # rotations[0] is a list of each (x,y,z)
    # here I am adding each new point to the other rotation queues
    rotations[1].append((y,-x,z))
    rotations[2].append((-x,-y,z))
    rotations[3].append((-y,x,z))
    rotations[4].append((x,-y,-z))
    rotations[5].append((-y,-x,-z))
    rotations[6].append((-x,y,-z))
    rotations[7].append((y,x,-z))
    rotations[8].append((z,y,-x))
    rotations[9].append((z,x,y))
    rotations[10].append((z,-y,x))
    rotations[11].append((z,-x,-y))
    rotations[12].append((-z,x,-y))
    rotations[13].append((-z,-y,-x))
    rotations[14].append((-z,-x,y))
    rotations[15].append((-z,y,x))
    rotations[16].append((y,z,x))
    rotations[17].append((x,z,-y))
    rotations[18].append((-y,z,-y))
    rotations[19].append((-x,z,-y))
    rotations[20].append((x,-z,y))
    rotations[21].append((-y,-z,x))
    rotations[22].append((-x,-z,-y))
    rotations[23].append((y,-z,-x))
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
        for (x,y,z) in rotations[0]:
            rotations = addRotations(rotations,x,y,z)
        # store the container
        scanners.append(rotations)
        pass
    else:
        # add the line to the first rotation
        rotations[0].append(tuple(map(lambda x: int(x),line.split(","))))
    #print(line)
# make the 23 other rotations last time
for (x,y,z) in rotations[0]:
    rotations = addRotations(rotations,x,y,z)
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
# 6 was the good rotation for scanner 1, found above
# scanner 1 is at (68, -1246, -43)
# scanner 4 relative to 1 is: (-88, 113, 1104)


results = []
for _ in scanners:
    results.append({
        "coord": (0,0,0),
        "relative_to": 0,
        "rotation": 0,
        "matches": []
    })

# relativeTo = 0
# lastRotation = 0
# for i in range(len(scanners)):
#     print(">>>>> iteration:", i)
#     relativeTo = i
#     originPoints = scanners[relativeTo][lastRotation] # compare everything to this
#     doBreak = False
#     for origin in originPoints:
#         #origin = originPoints[0] # first point of the origin scanner
#         if doBreak: break
#         for scanner in range(0,5):
#             if scanner == relativeTo: continue
#             if scanner == 0: continue
#             if len(results[scanner]["matches"]) > 0: continue
#             if doBreak: break
#             print("-- SCANNER " + str(scanner) + " --")
#             if scanner == 3:
#                 print("scanner 3, relativeto is:", relativeTo)
#             rotation = 0
#             for rotationSet in scanners[scanner]:
#                 if doBreak: break
#                 for point in rotationSet: 
#                     # take p1 from p0
#                     modifier = (origin[0]-point[0], origin[1]-point[1], origin[2]-point[2])
#                     matches = []
#                     for p in rotationSet:
#                         test = (modifier[0] + p[0], modifier[1] + p[1], modifier[2] + p[2])
#                         if test in originPoints:
#                             matches.append(test)
#                     if len(matches) >= 12:
#                         print("found a good one!")
#                         print("rotation: ", rotation)
#                         print("position of scanner "+str(scanner)+" relative to "+str(relativeTo)+":", modifier)
#                         print("overlapping points:")
#                         results[scanner]["coord"] = modifier
#                         results[scanner]["relative_to"] = relativeTo
#                         results[scanner]["rotation"] = rotation
#                         results[scanner]["matches"] = matches.copy()
#                         for m in matches:
#                             print(m)
#                         relativeTo = scanner
#                         doBreak = True
#                         break
#                 rotation += 1

# lastRotation = 0
# newMatchTotal = 0
# doneCompared = [set(),set(),set(),set(),set()]
# for scanner in range(len(scanners)):
#     doBreak = False # this lets me break out of the inner loops and start this one for a new scanner
#     # let's compare this scanner to another scanner, but skip 0
#     # (I don't want to compare 0 to anything)
#     if scanner == 0:
#         continue
#     for relativeTo in range(len(scanners)):
#         # don't compare the scanner to itself:
#         if scanner == relativeTo:
#             continue
#         #if doBreak: break
#         if relativeTo in doneCompared[scanner]:
#             continue
#         print("Comparing "+str(scanner)+" to "+str(relativeTo))
#         doneCompared[scanner].add(relativeTo)
#         print(doneCompared)
#         originPoints = scanners[relativeTo][lastRotation] # compare everything to this
#         for origin in originPoints:
#             if doBreak: break
#             rotation = 0
#             for rotationSet in scanners[scanner]:
#                 if doBreak: break
#                 for point in rotationSet: 
#                     # take p1 from p0
#                     modifier = (origin[0]-point[0], origin[1]-point[1], origin[2]-point[2])
#                     matches = []
#                     for p in rotationSet:
#                         test = (modifier[0] + p[0], modifier[1] + p[1], modifier[2] + p[2])
#                         if test in originPoints:
#                             matches.append(test)
#                     if len(matches) >= 12:
#                         print("found a good one!")
#                         print("rotation: ", rotation)
#                         print("position of scanner "+str(scanner)+" relative to "+str(relativeTo)+":", modifier)
#                         print("overlapping points:")
#                         results[scanner]["coord"] = modifier
#                         results[scanner]["relative_to"] = relativeTo
#                         results[scanner]["rotation"] = rotation
#                         results[scanner]["matches"] = matches.copy()
#                         print("Result of comparing "+str(scanner)+" to "+str(relativeTo)+" is: " + str(len(matches))+ " matches")
#                         newMatchTotal += len(matches)
#                         #for m in matches:
#                         #    print(m)
#                         doBreak = True
#                         break
#                 rotation += 1

# print("mmm: ", newMatchTotal)




# given that we know position of 4 relative to 1,
# to get the position of 4 relative to 0,
# look at the rotation that 1 is, compared to 0 => 6
# in my rotations creation, this is:
# rotations[6].append((-x,y,-z))
# so apply that to the coordinates of 4 relative to 1, before adding them
# 4 rel to 1: (88, 113, -1104)
# apply: (-88, 113, 1104)
# add to 1 which is (68, -1246, -43)
# (-88, 113, 1104) +
# (68, -1246, -43) =
# (-20, -1133, 1061) # correct!

def getConv(rotation, t):
    x = t[0]
    y = t[1]
    z = t[2]
    if rotation == 0: return (x,y,x)
    if rotation == 1: return (y,-x,z)
    if rotation == 2: return (-x,-y,z)
    if rotation == 3: return (-y,x,z)
    if rotation == 4: return (x,-y,-z)
    if rotation == 5: return (-y,-x,-z)
    if rotation == 6: return (-x,y,-z) # <<< rotation 6 # given x,y,z return -x,y,-z
    if rotation == 7: return (y,x,-z)
    if rotation == 8: return (z,y,-x)
    if rotation == 9: return (z,x,y)
    if rotation == 10: return (z,-y,x)
    if rotation == 11: return (z,-x,-y)
    if rotation == 12: return (-z,x,-y)
    if rotation == 13: return (-z,-y,-x)
    if rotation == 14: return (-z,-x,y)
    if rotation == 15: return (-z,y,x)
    if rotation == 16: return (y,z,x)
    if rotation == 17: return (x,z,-y)
    if rotation == 18: return (-y,z,-y)
    if rotation == 19: return (-x,z,-y)
    if rotation == 20: return (x,-z,y)
    if rotation == 21: return (-y,-z,x)
    if rotation == 22: return (-x,-z,-y)
    if rotation == 23: return (y,-z,-x)

# 4 can see 1
# 1 is positioned relative to 0
# need to change 4 so it is also relative to 0
# oldCoord = results[4]["coord"]
# print("oldCoord:", oldCoord)
# conv = getConv(results[1]["rotation"], oldCoord)
# print("conv:", conv)
# toScanner = results[1]["coord"]
# newCoord = (toScanner[0]+conv[0], toScanner[1]+conv[1], toScanner[2]+conv[2])
# results[4]["coord"] = newCoord
# results[4]["relative_to"] = 0

# is there a new way to do it ...
# find a scanner (e.g. 1) with matches relative 0
# reposition that one's coords and beacons it can see, relative to 0
# find another scanner that matches that one (e.g. 4)
# reposition that one's coords and beacons, relative to 0

# this procedure can be applied to all the matches of 4 relative to 1,
# so that I get the matches of 4 relative to 0
# TODO: I need a master matches SET, so that beacons that are spotted by several scanners are not counted twice.

toScanner = 0
for i in range(1, len(scanners)):
    doBreak = False # this lets me break out of the inner loops and start this one for a new scanner
    for compareThisScanner in range(len(scanners)):
        if doBreak: break
        # let's compare this scanner to another scanner, but skip 0
        # (I don't want to compare 0 to anything)
        if compareThisScanner == 0:
            continue
        # don't compare the scanner to itself:
        if compareThisScanner == toScanner:
            continue
        if toScanner == 3: # 3 also has points that overlap with 1, but the example talks about 4 so let's work with that
            continue
        if compareThisScanner == 3:
            continue
        # for now don't repeat:
        if len(results[compareThisScanner]["matches"]) > 0:
            continue
        print("Comparing "+str(compareThisScanner)+" to "+str(toScanner))
        toScannerPoints = scanners[toScanner][0] # compare everything to this non-rotated set
        for toScannerPoint in toScannerPoints:
            if doBreak: break
            rotation = 0
            for rotationSet in scanners[compareThisScanner]:
                if doBreak: break
                for compareThisScannerPoint in rotationSet: 
                    # take p1 from p0
                    absPosition = (toScannerPoint[0]-compareThisScannerPoint[0], toScannerPoint[1]-compareThisScannerPoint[1], toScannerPoint[2]-compareThisScannerPoint[2])
                    matches = []
                    for p in rotationSet:
                        test = (absPosition[0] + p[0], absPosition[1] + p[1], absPosition[2] + p[2])
                        if test in toScannerPoints:
                            matches.append(test)
                    if len(matches) >= 12:
                        print("found a good one!")
                        print("rotation: ", rotation)
                        print("position of scanner "+str(compareThisScanner)+" relative to "+str(toScanner)+":", absPosition)
                        results[compareThisScanner]["coord"] = absPosition
                        results[compareThisScanner]["relative_to"] = toScanner
                        results[compareThisScanner]["rotation"] = rotation
                        results[compareThisScanner]["matches"] = matches.copy()
                        print("Result of comparing "+str(compareThisScanner)+" to "+str(toScanner)+" is: " + str(len(matches))+ " matches")
                        print("overlapping points:")
                        for m in matches:
                            print(m)
                        # try to shift it
                        # 4 can see 1
                        # 1 is positioned relative to 0
                        # need to change 4 so it is also relative to 0
                        oldCoord = results[compareThisScanner]["coord"]
                        print(" oldCoord:", oldCoord)
                        conv = getConv(results[toScanner]["rotation"], oldCoord)
                        print(" conv:", conv)
                        toScanner = results[toScanner]["coord"]
                        newCoord = (toScanner[0]+conv[0], toScanner[1]+conv[1], toScanner[2]+conv[2])
                        results[compareThisScanner]["coord"] = newCoord
                        print(" newCoord:", newCoord)
                        results[compareThisScanner]["relative_to"] = 0
                        
                        # should all of 4's points also go through this process?
                        # this doesn't work, the adjustment params are wrong
                        # for i, v in enumerate(matches):
                        #     matches[i] = (matches[i][0]+conv[0], matches[i][1]+conv[1], matches[i][2]+conv[2])
                        # results[compareThisScanner]["matches"] = matches.copy()

                        # pass on to the next
                        toScanner = compareThisScanner
                        doBreak = True
                        break
                rotation += 1





















# scanner 4 relative to 1 is:
# 88,113,-1104
# scanner 1 relative to 0 is:
# (68, -1246, -43)
# so scanner 4 rel to 0 is:
# add position of 1
# 

# need: -20,-1133,1061

matchCount = 0
for i, result in enumerate(results):
    print("Scanner:",i)
    print(result)
    matchCount += len(result["matches"])
print(matchCount)