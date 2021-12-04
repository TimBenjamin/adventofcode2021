import re

def getNumbers(filename):
    with open(filename) as file:
        line = file.readline().rstrip()
        strings = line.split(",")
        numbers = []
        for s in strings:
            numbers.append(int(s))
    return numbers

def getBoards(filename):
    boards = []
    board = []
    with open(filename) as file:
        next(file)
        next(file)
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                # make a new board
                boards.append(board)
                board = []
            else:
                # turn the line into a list and append it to the current board
                row = re.split("\s+", line)
                board.append(row)
    boards.append(board)
    return boards

def checkBoardForWin(board):
    # found numbers are turned into X
    cols = ["", "", "", "", ""]
    for i in range(len(board)):
        if "".join(board[i]) == "XXXXX":
            return True
        for j in range(len(board[i])):
            cols[j] += board[i][j]
            if cols[j] == "XXXXX":
                return True
    return False

def tickBoard(number, board):
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            num = row[j]
            if num != "X" and int(num) == number:
                board[i][j] = "X"
    return board

def getScore(number, board):
    total = 0
    for row in board:
        for num in row:
            if num != "X":
                total += int(num)
    return total * number

def doNumber(number, boards):
    for i in range(len(boards)):
        boards[i] = tickBoard(number, boards[i])
    return boards

def removeWinningBoards(boards):
    newBoards = []
    for i in range(len(boards)):
        if checkBoardForWin(boards[i]):
            pass
        else:
            newBoards.append(boards[i])
    return newBoards

def checkForWinners(boards):
    for i in range(len(boards)):
        if checkBoardForWin(boards[i]):
            return i
    return False