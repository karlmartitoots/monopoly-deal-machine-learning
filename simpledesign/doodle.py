import numpy as np
from monopolydeal import giveCards

hands = np.zeros((2, 106))

giveCards([0,2,59,38,105,3],0)

print(all(hands[0][[0,2,59,38,105,3]]))

