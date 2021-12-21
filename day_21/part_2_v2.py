import sys

def move(pos, roll):
    return ((pos + roll -1) % 10) + 1

def gameTurn(g, currentPlayer, wins):
    global cache

    currentPlayer = (currentPlayer + 1) % 2

    if g[0][1] >= 21:
        return (1,0)
    elif g[1][1] >= 21:
        return (0,1)

    k = (g[0][0], g[1][0], g[0][1], g[1][1], currentPlayer)
    if k in cache:
        #print("cache hit for k:",k)
        return cache[k]

    p1wins = 0
    p2wins = 0
    for d1 in range(1,4):
        for d2 in range(1,4):
            for d3 in range(1,4):
                game = [x for x in g]
                #print(game, currentPlayer, roll)
                roll = d1+d2+d3
                newPosition = move(game[currentPlayer][0], roll)
                score = game[currentPlayer][1] + newPosition
                game[currentPlayer] = (newPosition, score)
                wins = gameTurn(game, currentPlayer, wins)
                p1wins += wins[0]
                p2wins += wins[1]
    cache[k] = (p1wins, p2wins)
    return cache[k]

playerOnePosition = int(sys.stdin.readline().strip()[28:])
playerTwoPosition = int(sys.stdin.readline().strip()[28:])
currentPlayer = 1 # gameTurn() will immediately flip the player to 0
cache = {}

# game:
# [
# player 1: (position, score),
# player 2: (position, score)
# ]
game = [(playerOnePosition,0),(playerTwoPosition,0)]
wins = gameTurn(game, currentPlayer, (0,0))
print("wins: ", wins)
print("player 1 wins: " + str(wins[0]) + " / player 2 wins: " + str(wins[1]))

wins = sorted(wins)
print(wins[1])
