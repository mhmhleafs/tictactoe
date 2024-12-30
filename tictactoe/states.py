from functions import *
from Board import *

def start_game(debug):
    board = Board()
    win = False
    turn = 1 #X starts (modulo is 1)
    move = -1

    board.print()

    while win == False:
        #turn cluster:
        move = get_move(board, move, turn)
        board.makeMove(move, turn)
        board.print(move,turn,debug)
        
        if(board.winner != None):
            board.print(move, turn, debug)
            board.printWin()
            return
        turn += 1