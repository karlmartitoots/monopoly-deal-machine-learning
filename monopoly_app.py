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
    return [np.zeros((7,)),       #0. browns
            np.zeros((7,)),       #1. dark blues
            np.zeros((9,)),       #2. greens
            np.zeros((9,)),       #3. light blues
            np.zeros((9,)),       #4. oranges
            np.zeros((9,)),       #5. purple
            np.zeros((11,)),      #6. rail roads
            np.zeros((9,)),       #7. reds
            np.zeros((7,)),       #8. utilites
            np.zeros((9,)),       #9. yellows
            np.zeros((67,))]      #10. money


def create_game_state(n_players):
    board = create_board()
    game_state = [np.ones((110,)),     #0. deck
                  [],                  #1. boards
                  [],                  #2. hands 
                  np.zeros((110,))]    #3. cards down
    for i in range(n_players):
        game_state[1].append(board)
        game_state[2].append(np.zeros(110,))
    return game_state


def initialize_params(n_players):
    global nPlayers
    global gameState
    global choices
    global deckWeights
    global firstRound
    global gameOn
    nPlayers = n_players
    gameState = create_game_state(n_players)
    choices = np.arange(110)
    deckWeights = gameState[0]/sum(gameState[0])
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


nPlayers = 0
gameState = []
choices = np.array([])
deckWeights = np.array([])
gameOn = False
firstRound = False
initialize_params(n_players=2)
