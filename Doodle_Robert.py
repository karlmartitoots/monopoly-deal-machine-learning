import numpy as np

f = open('allCards.txt','r')
deck = np.array([int((line.split(',')[1]).strip()) for line in f])
f.close()

print(deck)