import numpy as np


class Board():
    '''
    board:
    [brown1, brown2, house1, hotel1, brown3, brown4, house2, hotel2, brown5,  } 9
     blue1 , ...                                                           ,  } 9
     pistacchio1, ...                                                      ,  } 5 
     lightblue1, ...                                                       ,  } 11
     purple1, ...                                                          ,  } 11
     orange1, ...                                                          ,  } 11
     red1, ...                                                             ,  } 11
     yellow1, ...                                                          ,  } 11
     green1, ...                                                           ,  } 11
     black1, ...                                                            ] } 9

    '''
    def __init__(self):
        self.board = np.zeros((108,))

    def getCard(self, boardIndex, cardIndex):
        self.board[boardIndex] = cardIndex
    
    def giveCard(self, boardIndex):
        self.board[boardIndex] = 0