import numpy as np
size=1000000
cards = np.random.choice(['SS','HH','SH'],size,p=[0.2, 0.3, 0.5])
idx = np.random.choice(2,size)

S = 0
HS = 0
for i in range(0,size):
    if cards[i][idx[i]]=='S':
        S += 1
        if cards[i][1-idx[i]]=='H':
            HS += 1
print('S: ', S)
print('HS: ', HS)
print('prob: ', HS/S)
