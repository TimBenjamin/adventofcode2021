import sys

steps = []
while line := sys.stdin.readline().strip():
    # on x=-20..26,y=-36..17,z=-47..7
    # off x=-10547..1784,y=17386..41752,z=71103..94652
    line = line.split(" ")
    state = line[0] # on/off
    xyz = line[1].split(",")
    
    ranges = []
    for i in range(3):
        s = xyz[i].split("=")[1].split("..")
        ranges.append((int(s[0]), int(s[1])))
    
    step = {
        "state": state,
        "ranges": ranges
    }

    steps.append(step)

on = set()
for step in steps:
    if step["ranges"][0][0] < -50 or step["ranges"][0][0] > 50:
        print("x too big:",step["ranges"][0][0])
        continue
    if step["ranges"][1][0] < -50 or step["ranges"][1][0] > 50:
        print("y too big:",step["ranges"][1][0])
        continue
    if step["ranges"][2][0] < -50 or step["ranges"][2][0] > 50:
        print("z too big:",step["ranges"][2][0])
        continue
    for x in range(step["ranges"][0][0], step["ranges"][0][1]+1):
        for y in range(step["ranges"][1][0], step["ranges"][1][1]+1):
            for z in range(step["ranges"][2][0], step["ranges"][2][1]+1):
                if step["state"] == "on":
                    on.add((x,y,z))
                else:
                    if (x,y,z) in on:
                        on.remove((x,y,z))

print(len(on))