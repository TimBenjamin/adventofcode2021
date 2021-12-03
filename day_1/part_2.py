

incs = 0
start = False
last = 0
count = 0
window = []

with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        
        if(count < 3):
            count = count + 1
            window.append(int(line))
        else:
            s = sum(window)
            print("sum is:" + str(s))

            w = window[1:]
            w.append(int(line))
            window = w
            
            if(start):
                if s > last:
                    incs = incs + 1
                last = s
            else:
                start = True
                last = s

s = sum(window)
print("sum is:" + str(s))
if s > last:
    incs = incs + 1

print(incs)