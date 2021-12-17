with open("input.txt") as file:
    input = file.readline().strip()
c = input[13:].split(", ")

targetX = tuple(map(lambda x: int(x),c[0][2:].split("..")))
targetY = tuple(map(lambda x: int(x),c[1][2:].split("..")))

# fire with ANY velocity and see if we go into the target or miss it
def tryVelocity(velocityX, velocityY):
    #print("Trying: ", velocityX, velocityY)
    probeX, probeY = 0, 0
    step = 1
    maxY = probeY
    while True:
        #print("Step: " + str(step) + " - probe x,y position: ", probeX, probeY)

        # each step:
        # The probe's x position increases by its x velocity.
        probeX += velocityX
        
        # The probe's y position increases by its y velocity.
        probeY += velocityY

        # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
        if velocityX < 0:
            velocityX += 1
        elif velocityX > 0:
            velocityX -= 1

        # Due to gravity, the probe's y velocity decreases by 1.
        velocityY -= 1
        
        # for now we are interested in how high it goes:
        if probeY > maxY:
            maxY = probeY

        # is the probe in the target area?
        # (targetX is always positive and targetY is always negative)
        if probeX >= targetX[0] and probeX <= targetX[1] and probeY >= targetY[0] and probeY <= targetY[1]:
            #print("We hit the target! Max height was:", maxY)
            return maxY

        # is the probe beyond the target area?
        if probeX > targetX[1] and velocityX > 0:
            #print("Gone too far in X direction and not coming back.")
            return False
        if probeX < targetX[0] and velocityX < 0:
            #print("Going in wrong X direction, will never hit target.")
            return False
        if probeY < targetY[0]:
            #print("Below the target and falling.")
            return False
        if velocityX == 0 and (probeX < targetX[0] or probeX > targetX[1]):
            #print("The probe isn't moving horizontally, cannot reach target.")
            return False

        step += 1

maxY = 0
for x in range(1, targetX[1]):
    for y in range(targetY[0], 1000):
        result = tryVelocity(x, y)
        if result is not False and result > maxY:
            print("New high point:", result)
            maxY = result

print("Best high point:", maxY)