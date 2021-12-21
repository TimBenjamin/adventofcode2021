import sys

playerOnePosition = int(sys.stdin.readline().strip()[28:])
playerTwoPosition = int(sys.stdin.readline().strip()[28:])

dieSides = 100
boardSpots = 10

currentPlayer = 0
players = [{"position": playerOnePosition, "score": 0},{"position": playerTwoPosition, "score": 0}]

rollCount = 0
lastRoll = -1
while True:
    roll = (((lastRoll+1)%dieSides)+1, ((lastRoll+2)%dieSides)+1, ((lastRoll+3)%dieSides)+1)
    lastRoll += 3
    rollCount += 3
    
    players[currentPlayer]["position"] += sum(roll)
    players[currentPlayer]["position"] = ((players[currentPlayer]["position"]-1) % 10) + 1
    players[currentPlayer]["score"] += players[currentPlayer]["position"]
    
    print("Roll " + str(rollCount) + " - player " + str(currentPlayer+1) + " rolls " + str(sum(roll)) + " and moves to position " + str(players[currentPlayer]["position"]) + " and now has score: " + str(players[currentPlayer]["score"]))
    if players[currentPlayer]["score"] == 1000:
        print("player " + str(currentPlayer+1) + " wins!")
        currentPlayer = (currentPlayer + 1) % 2
        print("solution: " + str(players[currentPlayer]["score"] * rollCount))
        break

    currentPlayer = (currentPlayer + 1) % 2


    
