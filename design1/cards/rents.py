
rents = {
    "brown1": 1,
    "brown2": 2,
    "blue1": 3,
    "blue2": 8,
    "green1": 2,
    "green2": 4,
    "green3": 7,
    "lightblue1": 1,
    "lightblue2": 2,
    "lightblue3": 3,
    "orange1": 1,
    "orange2": 3,
    "orange3": 5,
    "purple1": 1,
    "purple2": 2,
    "purple3": 4,
    "black1": 1,
    "black2": 2,
    "black3": 3,
    "black4": 4,
    "red1": 2,
    "red2": 3,
    "red3": 6,
    "pistacchio1": 1,
    "pistacchio2": 2,
    "yellow1": 2,
    "yellow2": 4,
    "yellow3": 6
}
def getRent(color, amount):
    return rents[color + str(amount)]