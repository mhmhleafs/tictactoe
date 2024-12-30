from constants import *

MOVE_ROW = lambda x : int(x/3)
MOVE_COL = lambda x : x % 3

COORD_TO_ARRAY = lambda row, col : 3*row + col

#determines if the current turn belongs to X or O
def current_turn(turn):
    if(turn % 2 == 1):
        return 'X'
    else:
        return 'O'
    
#gets the user's next move
def get_move(board, move, turn):
    moveChar = input(f"{turn}: Select space: ")

    while(True):
        if(moveChar.lower() not in INPUTS):
            board.print(move, turn - 1) #display colour from prev. turn, since no new moves
            moveChar = input(f"{turn}: Invalid input. Select valid space: ")
        elif(not board.isOpen(INPUT_MAP[moveChar])):
            board.print(move, turn - 1) #display colour from prev. turn, since no new moves
            moveChar = input(f"{turn}: Space taken. Select open space: ")
        else:
            return INPUT_MAP[moveChar]
        
def dummy(anything):
    return anything
    
def boldify(text):
    return (colour.BOLD + str(text) + colour.END)

def redify(text):
    return (colour.RED + boldify(text) + colour.END)

def bluify(text):
    return colour.BLUE + boldify(text) + colour.END

def selected(text):
    return (colour.GREEN + boldify(text) + colour.END)