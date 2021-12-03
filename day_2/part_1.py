
h = 0 # horizontal position
d = 0 # depth

with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        dir, amt = line.split(" ")
        amt = int(amt)
        if dir == "forward":
            h += amt
        elif dir == "down":
            d += amt
        elif dir == "up":
            d -= amt

print("final depth: " + str(d))
print("final position: " + str(h))

solution = d * h
print(solution)

