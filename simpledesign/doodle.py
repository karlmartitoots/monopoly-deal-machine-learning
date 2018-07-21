import numpy as np

deck = np.ones((106,))
deck[0:106:4] = 0

print(np.random.choice(np.where(deck==1)[0]))