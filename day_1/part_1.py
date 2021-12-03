

incs = 0
start = False
last = 0
with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        if(start):
            if int(line) > last:
                print(line + " is more than " + str(last))
                incs = incs + 1
            last = int(line)
        else:
            start = True
            last = int(line)

    
print(incs)