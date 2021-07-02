from tictactoe  import *

# print(initial_state())
X = "X"
O = "O"
# b = [[X, EMPTY, EMPTY],
#     [EMPTY, O, EMPTY],
#     [EMPTY, EMPTY, X]]

b = [
    [O, X, O],
    [X, O, O],
    [O, X, X],
    ]

    # [['X', 'O', None], 
    # [None, 'O', None], 
    # [None, None, 'X']]

# print(player(b))
# print(actions(b))
# print(result(b, (2,2)))
# print(winner(b))
# 0,2 -> 
# 1,1 -> 
# 2,0
print(winner(b))