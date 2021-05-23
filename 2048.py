import numpy as np
import random

board = np.zeros((4,4))

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
