from funcs import getBoards, getScore, doNumber, checkForWinners, getNumbers

filename = "input.txt"

numbers = getNumbers(filename)
boards = getBoards(filename)

# run the game:
for number in numbers:
    boards = doNumber(number, boards)
    i = checkForWinners(boards)
    if i != False:
        winningBoard = boards[i]
        print("Found a winning board!", winningBoard)
        score = getScore(number, winningBoard)
        print("Score:", score)
        break
