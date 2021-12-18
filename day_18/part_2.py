import sys
from math import ceil, floor

# would be nice to split on anything that is not a number, and turn the numbers into ints
def parseInput(input):
    fish = []
    input = list(input)
    while len(input) > 0:
        c = input.pop(0)
        if c.isdigit():
            if len(input) > 0 and input[0].isdigit():
                c += input.pop(0)
            fish.append(int(c))
        elif c != ",":
            fish.append(c)
    return fish

def processFish(fish):
    # first check for any explodes
    newFish = []
    bcount = 0
    while len(fish) > 0:
        i = fish.pop(0)
        if i == "[":
            bcount += 1
        elif i == "]":
            bcount -= 1
        
        if bcount == 5:
            # do explode
            pair = []
            # hopefully the next two elements are just numbers in the pair...
            pair.append(fish.pop(0))
            pair.append(fish.pop(0))
            #print(" --> explode pair: ", pair)
            # the pair's left value is added to the first regular number to the left of the exploding pair (if any)
            for k, v in reversed(list(enumerate(newFish))):
                if isinstance(v, int):
                    newFish[k] += pair[0]
                    break
            # the pair's right value is added to the first regular number to the right of the exploding pair (if any)
            for k, v in enumerate(fish):
                if isinstance(v, int):
                    fish[k] += pair[1]
                    break
            # the entire exploding pair is replaced with the regular number 0
            newFish.append(0)
            # remove the closing bracket that is hopefully there
            fish.pop(0)
            # now we just read the rest of fish onto newFish and start again
            while len(fish) > 0:
                newFish.append(fish.pop(0))
            return newFish
        else:
            newFish.append(i)
    
    # check for any splits
    fish = newFish
    newFish = []
    while(len(fish) > 0):
        i = fish.pop(0)
        if isinstance(i, int) and i > 9:
            # do split
            #print(" --> split: ", i)
            # replace it with a pair
            # the left element of the pair should be the regular number divided by two and rounded down
            # the right element of the pair should be the regular number divided by two and rounded up.
            newFish.append("[")
            newFish.append(int(floor(i/2)))
            newFish.append(int(ceil(i/2)))
            newFish.append("]")
            # now we just read the rest of fish onto newFish and start again
            while len(fish) > 0:
                newFish.append(fish.pop(0))
            return newFish
        else:
            newFish.append(i)
    return newFish
    
# turn a fish back into the input format string:
def packet(fish):
    pack = ""
    while len(fish) > 0:
        i = fish.pop(0)
        if i == "[":
            pack += i
        elif i == "]":
            pack += i
            if len(fish) > 0 and fish[0] != "]":
                pack += ","
        else: # int
            pack += str(i)
            if len(fish) > 0 and (isinstance(fish[0], int) or fish[0] == "["):
                pack += ","
    return pack

def findus(input):
    fish = parseInput(input)
    #print(">>> ", packet(fish.copy()))
    while True:
        s = len(fish)
        finger = processFish(fish)
        if len(finger) == s:
            break
        else:
            #print("    ", packet(finger.copy()))
            fish = finger
    #print("<<< ", packet(finger.copy()))
    return packet(finger)

def getMagnitude(input):
    # The magnitude of a pair is
    # 3 times the magnitude of its left element
    # plus
    # 2 times the magnitude of its right element
    # The magnitude of a regular number is just that number.
    # 
    # so ... replace all [x,y] with single numbers and see what we are left with
    fish = parseInput(input)
    while True:
        newFish = []
        while len(fish) > 1:
            i = fish.pop(0)
            if i == "[" and isinstance(fish[0], int):
                if isinstance(fish[1], int):
                    m = (3 * fish[0]) + (2 * fish[1])
                    newFish.append(m)
                    fish.pop(0) # remove first int
                    fish.pop(0) # remove second int
                    fish.pop(0) # remove ]
                    # just add the rest
                    while len(fish) > 0:
                        newFish.append(fish.pop(0))
                else:
                    newFish.append(i)
            else:
                newFish.append(i)
        if len(newFish) == 1:
            return newFish[0]
        fish = newFish

maxMag = 0
inputs = []
while line := sys.stdin.readline().strip():
    inputs.append(line)

print("inputs: ", inputs)

for i, x in enumerate(inputs):
    for j, y in enumerate(inputs):
        if i == j:
            continue
        captain = "[" + x + "," + y + "]"
        birdseye = findus(captain)
        magnitude = getMagnitude(birdseye)
        if magnitude > maxMag:
            maxMag = magnitude
        print("x: " + x + "   plus y: " + y + "   = " + str(magnitude))

        captain = "[" + y + "," + x + "]"
        birdseye = findus(captain)
        magnitude = getMagnitude(birdseye)
        if magnitude > maxMag:
            maxMag = magnitude
        print("y: " + y + "   plus x: " + x + "   = " + str(magnitude))

print("Max magnitude is:", maxMag)


