import sys

def run(z, d, c1, c2):
    cond = (z % 26 + c1) != d
    if c1 < 0:
        z //= 26
    if cond:
        z = 26 * z + d + c2

    return z

zs = {0: ()}
for idx, line in enumerate(sys.stdin):
    line = line.strip().split(" ")
    cmd = line[0]
    c1 = line[1]
    try:
        c1 = int(c1)
    except ValueError:
        pass  # 
    c2 = None
    if cmd != "inp":
        c2 = line[2]
        try:
            c2 = int(c2)
        except ValueError:
            pass  # 
    #c1, c2 = map(int, line.split())
    CAP = 26**4
    zs = {
        run(z, d, c1, c2): v + (d,)
        for z, v in zs.items() for d in range(1, 10) # reverse range for part 2
        if z <= CAP
    }

print("".join(str(c) for c in zs[0]))