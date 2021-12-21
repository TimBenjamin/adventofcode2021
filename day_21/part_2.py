import sys

playerOnePosition = int(sys.stdin.readline().strip()[28:])
playerTwoPosition = int(sys.stdin.readline().strip()[28:])

playerWins = [0,0]
currentPlayer = 0

# keep track only of active universes; when a universe wins, increment winCount and destroy it
# each of these games in "universes" is
# [
# player 1: (position, score),
# player 2: (position, score)
# ]
universes = [ [(playerOnePosition,0),(playerTwoPosition,0)] ]

# The only possible roll totals and the number of times they are rolled:
# 3: 1
# 4: 3
# 5: 6
# 6: 7
# 7: 6
# 8: 3
# 9: 1
# 27 universes are spawned on each player's turn

rolls = [3,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,9]
target = 21
winCache = [set(),set()]
# while True:
for _ in range(10):

    newUniverses = []
    
    for g in universes:
        for roll in rolls:
            c = str(g)+"-"+str(currentPlayer)+"-"+str(roll)
            #print(c)
            if c in winCache[0]:
                #print("First cache hit for player 1")
                playerWins[0] += 1
                continue
            elif c in winCache[1]:
                #print("First cache hit for player 2")
                playerWins[1] += 1
                continue
            #print("roll:", roll)
            game = [x for x in g]
            #print("game:", game)
            newPosition = game[currentPlayer][0] + roll
            newPosition = ((newPosition-1)%10)+1
            game[currentPlayer] = (newPosition, game[currentPlayer][1] + newPosition)
            #print(" --> ", game)
            if game[currentPlayer][1] >= target: # did the player win?
                winCache[currentPlayer].add(c)
                playerWins[currentPlayer] += 1
            else:
                c = str(game)+"-"+str(currentPlayer)+"-"+str(roll)
                if c in winCache[0]:
                    #print("cache hit for player 1")
                    playerWins[0] += 1
                    continue
                elif c in winCache[1]:
                    #print("cache hit for player 2")
                    playerWins[1] += 1
                    continue
                newUniverses.append(game)
            #print("newUniverses: ", len(newUniverses))
            #print()
    
    print("newUniverses: ", len(newUniverses))
    print("player 1 wins: " + str(playerWins[0]) + " / player 2 wins: " + str(playerWins[1]))

    if len(newUniverses) == 0:
        break

    currentPlayer = (currentPlayer + 1) % 2
    universes = newUniverses
    
    
    

    

    
