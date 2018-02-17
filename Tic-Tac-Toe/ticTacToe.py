import random


def drawBoard(board):
    # Function to print out board - line of strings printing board to console
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def playerInput():
    # User input to have letter type - Will return list with user letter first and computers second
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # First element is player letter, second element is computer
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def isWinner(bo, le):
    # Returns true if player has won, bo stands for board and le for letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))    # diagonal


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    # Return true if move is free on board (once passed)
    return board[move] == ' '


def turnOrder():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def getPlayerMove(board):
    # Lets player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def makeMove(board, letter, move):
    # Allows player and computer to make moves
    board[move] = letter


def chooseRandomMoveFromList(board, movesList):
    # Returns valid move from list onto board
    # Returns none if no valid move taken
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Given board and letter, determine a move and return
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Artificial intelligence Algorithm:
    # Step 1: Can we win in next move?
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Step 2: Can player win in next move?
            # If they can, block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Step 3: Take a corner when possible
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Step 4: Try to take center when possible
    if isSpaceFree(board, 5):
        return 5

    # Step 5: Else move through sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return true if every space has been taken, otherwise return false
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def playAgain():
    # True is player plays again, else it will be false
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# Everything that doesn't require separate functions
def play():
    print('Welcome!')

    while True:
        # Resets the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = playerInput()  # function on line 22

        turn = turnOrder()

        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Player's turn.
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                # Computer's turn.
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('You have lost the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

        if not playAgain():
            break
play()
