import numpy as np
import random

deck = {
    "dealbreaker1": True,
    "dealbreaker2": True,
    "debtcollector1": True,
    "debtcollector2": True,
    "debtcollector3": True,
    "doublerent1": True,
    "doublerent2": True,
    "forceddeal1": True,
    "forceddeal2": True,
    "forceddeal3": True,
    "placehouse1": True,
    "placehouse2": True,
    "placehouse3": True,
    "placehotel1": True,
    "placehotel2": True,
    "placehotel3": True,
    "sayno1": True,
    "sayno2": True,
    "sayno3": True,
    "birthday1": True,
    "birthday2": True,
    "birthday3": True,
    "passgo1": True,
    "passgo2": True,
    "passgo3": True,
    "passgo4": True,
    "passgo5": True,
    "passgo6": True,
    "passgo7": True,
    "passgo8": True,
    "passgo9": True,
    "passgo10": True,
    "slydeal1": True,
    "slydeal2": True,
    "slydeal3": True,
    "brown1": True,
    "brown2": True,
    "blue1": True,
    "blue2": True,
    "green1": True,
    "green2": True,
    "green3": True,
    "lightblue1": True,
    "lightblue2": True,
    "lightblue3": True,
    "orange1": True,
    "orange2": True,
    "orange3": True,
    "purple1": True,
    "purple2": True,
    "purple3": True,
    "black1": True,
    "black2": True,
    "black3": True,
    "black4": True,
    "red1": True,
    "red2": True,
    "red3": True,
    "pistacchio1": True,
    "pistacchio2": True,
    "yellow1": True,
    "yellow2": True,
    "yellow3": True,
    "rainbow1": True,
    "rainbow2": True,
    "bluegreen": True,
    "lightbluebrown": True, 
    "orangepurple1": True, 
    "orangepurple2": True, 
    "greenblack": True,
    "lightblueblack": True, 
    "pistacchioblack": True,
    "redyellow1": True,
    "redyellow2": True,
    "rainbowrent1": True,
    "rainbowrent2": True,
    "rainbowrent3": True,
    "bluegreenrent1": True,
    "bluegreenrent2": True,
    "lightbluebrownrent1": True,
    "lightbluebrownrent2": True,
    "orangepurplerent1": True, 
    "orangepurplerent2": True, 
    "pistacchioblackrent1": True, 
    "pistacchioblackrent2": True, 
    "redyellowrent1": True, 
    "redyellowrent2": True, 
    "10m": True, 
    "1m": True, 
    "1m": True, 
    "1m": True, 
    "1m": True, 
    "1m": True, 
    "1m": True, 
    "2m": True, 
    "2m": True, 
    "2m": True, 
    "2m": True, 
    "2m": True, 
    "3m": True, 
    "3m": True, 
    "3m": True, 
    "4m": True, 
    "4m": True, 
    "4m": True, 
    "5m": True, 
    "5m": True
}
available = []
for card, cardInDeck in deck.items():
    if cardInDeck:
        available.append(card)
chosen = random.sample(available,5)
for card in chosen:
    deck[card] = False
print(deck)