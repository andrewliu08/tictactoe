def displayBoard(board):
    for column in range(3):
        for row in range(3):
            print(board[column][row], end='')
        print('')

def makeMove(board, player, r, c):
    board[r][c] = player

def switchPlayer(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def eval(board):
    if checkWin(board, 'X'):
        return 1
    elif checkWin(board, 'O'):
        return -1
    elif checkTie(board):
        return 0
    else:
        return 10

def checkWin(board, player):
    win = False
   # check for horizontal win
    for row in range(3):
        count = 0
        for column in range(3):
            if board[row][column] !=  player:
                break
            else:
                count += 1
        if count == 3:
            win = True
            break

    # check for vertical win
    if not win:
        for column in range(3):
            count = 0
            for row in range(3):
                if board[row][column] !=  player:
                    break
                else:
                    count += 1
            if count == 3:
                win = True
                break

    # check for diagonal win
    if not win:
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            win = True
        elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
            win = True
        else:
            win = False
    return win

def checkTie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True

def bestMove(board, depth, player):
    # maximizing player
    if player == 'X':
        bestScore = -float("inf")
        # go through possible positions and find best score
        for row in range(3):
            for column in range(3):
                if board[row][column] == '-':
                    board[row][column] = player
                    score = minimax(board, depth-1, switchPlayer(player))
                    board[row][column] = '-'
                    if score > bestScore:
                        bestScore = score
                        move = (row,column)
        return move
    # minimizing player
    else:
        bestScore = float("inf")
        # go through possible positions and find best score
        for row in range(3):
            for column in range(3):
                if board[row][column] == '-':
                    board[row][column] = player
                    score = minimax(board, depth-1, switchPlayer(player))
                    board[row][column] = '-'
                    if score < bestScore:
                        bestScore = score
                        move = (row,column)
        return move

def minimax(board, depth, player):
    tiePoints = 0
    staticEval = eval(board)
    # player has winning position
    if depth == 0 or staticEval != 10:
        return staticEval
    # maximizing player
    elif player == 'X':
        bestScore = -float("inf")
        # go through possible positions and find best score
        for row in range(3):
            for column in range(3):
                if board[row][column] == '-':
                    board[row][column] = player
                    score = minimax(board, depth-1, switchPlayer(player))
                    board[row][column] = '-'
                    if score > bestScore:
                        bestScore = score
        return bestScore
    # minimizing player
    else:
        bestScore = float("inf")
        # go through possible positions and find best score
        for row in range(3):
            for column in range(3):
                if board[row][column] == '-':
                    board[row][column] = player
                    score = minimax(board, depth-1, switchPlayer(player))
                    board[row][column] = '-'
                    if score < bestScore:
                        bestScore = score
        return bestScore


board = [['-' for j in range(3)] for i in range(3)]
human = ''
while human == '':
    human = input("Which piece will human play? [X, O]")
    if human != 'X' and human != 'O':
        human = ''
ai = switchPlayer(human)

turn = 'X'
count = 0
run = True
while run:
    print("%s's Turn" %turn)
    displayBoard(board)
    if turn == human:
        notAvailable = True
        while notAvailable:
            move = [int(x) for x in  input('Type coordinates of move separated by space: ').split()]
            if board[move[0]][move[1]] == '-':
                notAvailable = False
                makeMove(board, human, move[0], move[1])
        if checkWin(board, human):
            displayBoard(board)
            print("Human wins!")
            run = False
            break
    else:
        aimove = bestMove(board, 3,ai)
        makeMove(board, ai, aimove[0], aimove[1])
        if checkWin(board, ai):
            displayBoard(board)
            print("AI wins!")
            run = False
            break
    if checkTie(board):
        print("Tie")
        run = False

    turn = switchPlayer(turn)
    count += 1
