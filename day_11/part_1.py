men = ""
with open("input.txt") as file:
    while line := file.readline().strip():
        men += line

dirtyoldmen = list(map(int, list(men)))

def show(dirtyoldmen):
    for i, m in enumerate(dirtyoldmen):
        print(str(m)+" ", end="")
        if (i+1) % 10 == 0:
            print()
    print()

def findFlashers(dirtyoldmen, flashed):
    flashers = []
    for pos, pervert in enumerate(dirtyoldmen):
        if pervert > 9 and pos not in flashed:
            flashers.append(pos)
    return flashers

fsplats = [-1, +1, -9, -10, -11, +9, +10, +11]
lsplats = [+1, +10, +11, -9, -10]
rsplats = [-1, -10, -11, +9, +10]
flashes = 0
for step in range(100):
    dirtyoldmen = list(map(lambda x: x+1, dirtyoldmen))
    flashed = []
    while True:
        flashers = findFlashers(dirtyoldmen, flashed)
        if len(flashers) == 0:
            for pos, oldman in enumerate(dirtyoldmen):
                if oldman > 9:
                    dirtyoldmen[pos] = 0
            print("end of step", step+1)
            show(dirtyoldmen)
            break
        #print("found "+str(len(flashers))+" flashers, doing flash:\n")
        for flasher in flashers:
            flashed.append(flasher)
            dirtyoldmen[flasher] = 0
            flashes += 1
            if flasher % 10 == 0: splats = lsplats
            elif (flasher+1) % 10 == 0: splats = rsplats
            else: splats = fsplats
            for splat in splats:
                if flasher + splat >= 0 and flasher + splat <= 99 and dirtyoldmen[flasher + splat] != 0:
                    dirtyoldmen[flasher + splat] += 1

print(flashes)
