total = 0
with open("input.txt") as file:
    while line := file.readline().rstrip():
        _, output = line.split(" | ")
        output = sorted(output.split(" "))
        for o in output:
            l = len(o)
            if l == 2 or l == 4 or l == 3 or l == 7:
                total += 1
print(total)