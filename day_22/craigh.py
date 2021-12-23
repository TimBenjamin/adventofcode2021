import re
import sys

cuboids = {}

for line in (l.strip() for l in sys.stdin):
    sign = line.startswith("on")
    x0, x1, y0, y1, z0, z1 = (int(x) for x in re.findall("-?[0-9]+", line))

    new_cuboids = {}
    for ex_cuboid, ex_sign in cuboids.items():
        ex_x0, ex_x1, ex_y0, ex_y1, ex_z0, ex_z1 = ex_cuboid

        int_x0 = max(x0, ex_x0)
        int_x1 = min(x1, ex_x1)
        int_y0 = max(y0, ex_y0)
        int_y1 = min(y1, ex_y1)
        int_z0 = max(z0, ex_z0)
        int_z1 = min(z1, ex_z1)

        if int_x0 <= int_x1 and int_y0 <= int_y1 and int_z0 <= int_z1:
            k = (int_x0, int_x1, int_y0, int_y1, int_z0, int_z1)
            new_cuboids[k] = new_cuboids.get(k, 0) + (0 - ex_sign) #.get(k,0) will get the sign of the cube "k"[0 or 1] or 0, and it is adding 0 or -1 => thus turning it to 0
    
    if sign > 0:
        k = (x0, x1, y0, y1, z0, z1)
        new_cuboids[k] = new_cuboids.get(k, 0) + 1 # sets the sign for cuboid with key "k" to be 1
    
    for c, s in new_cuboids.items(): # (cubekey, sign)
        cuboids[c] = cuboids.get(c, 0) + s # adds c to cuboids; if it's there already, it just sets the sign to s; if it isn't, it gets set with sign s

total = 0
for cuboid, sign in cuboids.items():
    x0, x1, y0, y1, z0, z1 = cuboid
    total += (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sign

print(total)