def displayBoard(board):
    for column in range(3):
        for row in range(3):
            print(board[column][row].type, end='')
        print('')

def switchPlayer(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def checkWin(board, player):
    win = False
   # check for horizontal win
    for row in range(3):
        count = 0
        for column in range(3):
            if board[row][column].type !=  player:
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
                if board[row][column].type !=  player:
                    break
                else:
                    count += 1
            if count == 3:
                win = True
                break

    # check for diagonal win
    if not win:
        if board[0][0].type == player and board[1][1].type == player and board[2][2].type == player:
            win = True
        elif board[2][0].type == player and board[1][1].type == player and board[0][2].type == player:
            win = True
        else:
            win = False
    return win

def checkTie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j].type == '-':
                return False
    return True

def eval(board):
    if checkWin(board, 'X'):
        return 1
    elif checkWin(board, 'O'):
        return -1
    elif checkTie(board):
        return 0
    else:
        return 10

def bestMove(board, depth, player):
    # maximizing player
    if player == 'X':
        bestScore = -float("inf")
        # go through possible positions and find best score
        for row in range(3):
            for column in range(3):
                if board[row][column].type == '-':
                    board[row][column].type = player
                    score = minimax(board, depth-1, switchPlayer(player))
                    board[row][column].type = '-'
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
                if board[row][column].type == '-':
                    board[row][column].type = player
                    score = minimax(board, depth-1, switchPlayer(player))
                    board[row][column].type = '-'
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
                if board[row][column].type == '-':
                    board[row][column].type = player
                    score = minimax(board, depth-1, switchPlayer(player))
                    board[row][column].type = '-'
                    if score > bestScore:
                        bestScore = score
        return bestScore
    # minimizing player
    else:
        bestScore = float("inf")
        # go through possible positions and find best score
        for row in range(3):
            for column in range(3):
                if board[row][column].type == '-':
                    board[row][column].type = player
                    score = minimax(board, depth-1, switchPlayer(player))
                    board[row][column].type = '-'
                    if score < bestScore:
                        bestScore = score
        return bestScore
