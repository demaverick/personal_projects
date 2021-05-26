import numpy as np
import random

# Initializing the board with Zeros
board = np.zeros((4,4))

# Initializing a list which stores all the (i,j) coordinates in the board
# Which can be used to check what every block contains - Filled or not filled with a number
# So the Base condition would be if the tuple is empty the Game is over.
tuplelist = []
for i in range(4):
    for j in range(4):
        tuplelist.append((i,j))
i = 0
while(len(tuplelist) != 0):
    i+=1
    a = (random.choice(tuplelist))
    board[a[0],a[1]] = 2
    print(board)
    tuplelist.pop(tuplelist.index(a))
