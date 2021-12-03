
h = 0 # horizontal position
d = 0 # depth
a = 0 # aim

with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        dir, amt = line.split(" ")
        amt = int(amt)
        if dir == "forward":
            h += amt
            d += (a * amt)
        elif dir == "down":
            a += amt
        elif dir == "up":
            a -= amt

print("final depth: " + str(d))
print("final position: " + str(h))
print("final aim: " + str(a))

solution = d * h
print(solution)

