from funcs import getBoards, removeWinningBoards, tickBoard, checkBoardForWin, getScore, doNumber, checkForWinners, removeWinningBoards

numbers = [23,91,18,32,73,14,20,4,10,55,40,29,13,25,48,65,2,80,22,16,93,85,66,21,9,36,47,72,88,58,5,42,53,69,52,8,54,63,76,12,6,99,35,95,82,49,41,17,62,34,51,77,94,7,28,71,92,74,46,79,26,19,97,86,87,37,57,64,1,30,11,96,70,44,83,0,56,90,59,78,61,98,89,43,3,84,67,38,68,27,81,39,15,50,60,24,45,75,33,31]
boards = getBoards("input.txt")

#numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
#boards = getBoards("test_input.txt")

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
        print("length of boards after removing winners:", len(boards))
            


            
            


