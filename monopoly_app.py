import numpy as np
#TODO: fix gameState missing information
#TODO: how to make action cards work
#TODO: how to make card choices in hand
#TODO: how to make 1 to 3 moves
#TODO: neural input output
#TODO: over 7 cards
#TODO: empty hand - take 5
#TODO: end game conditions
#TODO: object-oriented cards


def create_board():
    return [np.zeros((7,)), 
            np.zeros((7,)), 
            np.zeros((9,)), 
            np.zeros((9,)), 
            np.zeros((9,)), 
            np.zeros((9,)), 
            np.zeros((11,)), 
            np.zeros((9,)), 
            np.zeros((7,)), 
            np.zeros((9,)),
            np.zeros((100,))]


def initialize_params(n_players):
    global nPlayers
    global choices
    global gameOn
    global deckWeights
    global gameState
    global firstRound
    nPlayers = n_players
    f = open('allCards.txt','r') #init deck
    deck = np.array([int((line.split(',')[1]).strip()) for line in f])
    f.close()
    choices = np.arange(58) # init choices
    deckWeights = deck/np.sum(deck) # init weights
    board = [np.zeros((7,)), np.zeros((7,)), np.zeros((9,)), np.zeros((9,)), np.zeros((9,), np.zeros((9,), np.zeros((11,), np.zeros((9,), np.zeros((7,), np.zeros((9,)]
    gameState = [deck, 
                 np.zeros((n_players,58)), 
                 np.zeros((n_players,58)), 
                 np.zeros((58,))] #deck, boards, hands, cards down
    gameOn = True
    firstRound = True


def draw_five_cards(player_index):
    for i in range(5):
            draw_card(player_index)


def draw_card(player_index):
    global choices
    global deckWeights
    global gameState
    card_index = np.random.choice(choices, p=deckWeights)
    gameState[0][card_index] -= 1
    gameState[1][player_index][card_index] += 1
    deckWeights = gameState[0]/np.sum(gameState[0])


choices = 0
nPlayers = 0
gameOn = False
deck = 0
deckWeights = 0
gameState = []
firstRound = False
initialize_params(n_players=2)


while gameOn:
    if firstRound:
        for player_index in range(nPlayers):
            draw_five_cards(player_index)
        
        for player_index in range(nPlayers):
            moves = 3
            


        firstRound = False

    break
    #for player in range(n_players):
         #one turn

print(gameState[1])