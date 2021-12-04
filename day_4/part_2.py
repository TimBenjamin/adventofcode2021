from funcs import getBoards, removeWinningBoards, getScore, doNumber, removeWinningBoards, getNumbers

filename = "input.txt"

numbers = getNumbers(filename)
boards = getBoards(filename)

# run the game:
for number in numbers:
    print("draw number", number)
    boards = doNumber(number, boards)
    newBoards = removeWinningBoards(boards)
    if len(newBoards) == 0:
        print("last board:", boards)
        print("score:", getScore(number, boards[0]))
        break
    else:
        boards = newBoards
            


            
            



