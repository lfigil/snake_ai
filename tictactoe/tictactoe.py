"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


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
    x_counter = 0
    o_counter = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_counter += 1
            elif board[i][j] == O:
                o_counter += 1
    
    # print(f"x: {x_counter}")
    # print(f"o: {o_counter}")
    
    if x_counter > o_counter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avail_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                avail_moves.add((i,j))
    
    if len(avail_moves) == 0:
        return 0

    return avail_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        if action in actions(board):
            copy_board = copy.deepcopy(board)
            i, j = action
            player_turn = player(board)
            copy_board[i][j] = player_turn
            print(copy_board)
            return copy_board
        else:
            raise IndexError
    except IndexError:
        print("Invalid move")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Hard code winning moves
    # row0
    if board[0][0] == board[0][1] == board[0][2] == X:
        return X
    elif board[0][0] == board[0][1] == board[0][2] == O:
        return O
    # row1
    elif board[1][0] == board[1][1] == board[1][2] == X:
        return X
    elif board[1][0] == board[1][1] == board[1][2] == O:
        return O
    # row2
    elif board[2][0] == board[2][1] == board[2][2] == X:
        return X
    elif board[2][0] == board[2][1] == board[2][2] == O:
        return O
    # col0
    elif board[0][0] == board[1][0] == board[2][0] == X:
        return X
    elif board[0][0] == board[1][0] == board[2][0] == O:
        return O
    # col1
    elif board[0][1] == board[1][1] == board[2][1] == X:
        return X
    elif board[0][1] == board[1][1] == board[2][1] == O:
        return O
    # col2
    elif board[0][2] == board[1][2] == board[2][2] == X:
        return X
    elif board[0][2] == board[1][2] == board[2][2] == O:
        return O
    # diagonal
    elif board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O
    # inverse diagonal
    elif board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    counter = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X or board[i][j] == O:
                counter += 1

    if counter < 9:
        return False
    else:
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    current_player = player(board)

def max_func(state):
        value = -math.inf
        if terminal(state):
            return utility(state)
        
        for action in actions(state):
            value = max(value, min_func(result(state, action)))
        
        return value

def min_func(state):
    value = math.inf
    if terminal(state):
        return utility(state)
    
    for action in actions(state):
        value = min(value, max_func(result(state, action)))
    
    return value

