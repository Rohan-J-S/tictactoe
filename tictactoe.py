"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from random import randint

X = "X"
O = "O"
EMPTY = None

# class node:
#     def __init__(parent , board , children, turn):
#         self.parent = parent 
#         self.board = board
#         self.children = children
#         self.turn = turn

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for row in board:
        for col in row:
            if col == "X":
                x += 1
            elif col == "O":
                o += 1
    if x == o and not(terminal(board)):
        return X
    elif x > o and not(terminal(board)):
        return O
    else:
        return None
            
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    
    res = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                res.add((i , j))
    # print(res)
    return res
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if action == None:
        # print(board)
    i = action[0]
    j = action[1]



    if i not in [0 , 1 , 2] or j not in [0 , 1 , 2] or board[i][j] != EMPTY:
        # print(i , j , "hi")
        raise Exception
    
    out = deepcopy(board)
    out[i][j] = player(board)
    return out
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        # print(row)
        if type(row) == int:
            pass
            # print(board , "hi")
        if O not in row and EMPTY not in row:
            return X
        elif X not in row and EMPTY not in row:
            return O 
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O
    
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X 
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O
    
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X 
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O
    
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        if winner(board) == X:
            print("x wins")
        else:
            print("o wins")
        return True 
    for row in board:
        if EMPTY in row:
            return False
        
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #only use when board is in terminal state
    if winner(board) == X:
        return 1 
    elif winner(board) == O:
        return -1 
    elif terminal(board):
        return 0
    else:
        arr = []
        for action in actions(board):
            arr.append(utility(result(board , action)))
        if player(board) == X:
            return max(arr)
        else:
            return min(arr)
    
    raise NotImplementedError


def minimax(board):
    if board == initial_state():
        starters = {}
        i = 0
        for action in actions(board):
            starters[i] = action
            i += 1
        return starters[randint(0 , 8)]
        
    #minimax func should return in tuple format not an integer computation of the minimum and maximum done saperately
    # recursively call minimax function until actions set is empty or terminal state is reached
    #if action set is empty return cordinates and store results in an array
    # if Xs turn maximise and if Os turn minimise 
    """
    Returns the optimal action for the current player on the board.
    """
    # recursively call the actions o0n the board until terminal state is reached
    # if its X turn, maximise the result and return
    # if its O turn , minimise the result and return

    # mini_value = -1000000
    # max_value = 1000000

    # terminal state
    # if terminal(board):
    #     return None
    
    # X player
    if player(board) == X:
        d = {}
        for action in actions(board):
            # arr.append(minimax(result(board , action)))
            # action_set.append(action)
            d[action] = utility(result(board , action))

        # print(d)
        current = (0 , 0)
        val = -100
        for key in d:
            # print(d[key] , val)
            if d[key] > val:
                current = key
                val = d[key]
        # print(current)
        return current    
        # return max(arr)

    else:
        d = {}
        for action in actions(board):
            # arr.append(minimax(result(board , action)))
            # action_set.append(action)
            d[action] = utility(result(board , action))
            
        # print(d)
        current = (0 , 0)
        val = 100
        for key in d:
            if d[key] < val:
                current = key
                val = d[key]
        # print(current)
        return current
        # raise NotImplementedError
# create a data structure
