from functions import *
from constants import *
import os

class Board:

    def __init__(self):
        self.state = [["a","b","c"],["d","e","f"],["g","h","i"]]
        self.winner = None
        self.winMethod = None
        self.finalStrings = None
    
    def __str__(self):
        return self.toString(self)

    def print(self, move = -1, turn = -1, debug=False):
        if(not debug):
            os.system("clear")

        if(move < 0 and turn < 0):
            print(self.toString())
        else:
            print(self.toString(move, turn))

    def toString(self, move = -1, turn = -1):
        if(self.winner != None):
            return f"{self.finalStrings[0]}\n{self.finalStrings[1]}\n{self.finalStrings[2]}"

        if(move < 0 and turn < 0):
            return self.getString_unselected()
        else:
            return self.getString(move, turn)
        
    def printWin(self):
        if(self.winner == False):
            print("It's a draw!")
        elif(self.winner != None):
            print(f"{self.winner} wins {WIN_METHOD_STRINGS[self.winMethod]}")
        
    def makeMove(self, move, turn):
        self.state[MOVE_ROW(move)][MOVE_COL(move)] = current_turn(turn)
        self.checkWin()

        if(turn == 9 and self.winner == None):
            self.winner = False
            self.finalizeStrings(-1)
    
    #positions in the form [[row1,col1],[row2,col2],[row3,col3]]
    def set_winner(board,positions, winner):
        for posn in positions:
            if(winner == 'X'):
                board.state[posn[0]][posn[1]] = redify('X')
            else:
                board.state[posn[0]][posn[1]] = bluify('O')

    def isOpen(self, move):
        if((self.state[MOVE_ROW(move)][MOVE_COL(move)]) not in OUTPUTS):
            return True
        return False
    

    def getString_unselected(self):
        string = ""
        i = 0
        for row in self.state:
            for col in row:
                if(str(col) not in OUTPUTS):
                    val = "-"
                else:
                    val = str(col)
                string += f"{LABEL[i]}{val} "
                i += 1
            string += "\n"
        return string

    #move is an integer 0-8 that represents an array index (2D)
    def getString(self, move, turn):
        string = ""
        for row in range(3):
            for col in range(3):
                string += LABEL[3*row + col]
                if(move == (3*row + col)):#0-2,3-5,6-8
                    if(turn % 2 == 1):
                        string += f"{redify(self.state[row][col])} "
                    else:
                        string += f"{bluify(self.state[row][col])} "
                else:
                    if(self.state[row][col] not in OUTPUTS):
                        string += "- "
                    else:
                        string += f"{self.state[row][col]} "
            string += "\n"
        return string

    def checkHorizontal(self, winSpot):
        for row in range(3):
            currRow = self.state[row]
            if currRow[0] == currRow[1] and currRow[1] == currRow[2]:
                self.winner = currRow[1]
                self.winMethod = 'H'
                return row
        return winSpot

    def checkVertical(self, winSpot):
        for i in range(3):
            if(self.state[0][i] == self.state[1][i] and self.state[1][i] == self.state[2][i]):
                self.winner = self.state[0][i]
                self.winMethod = 'V'
                return i
        return winSpot

    def checkDiagonal(self, winSpot):
        if(self.state[0][0] == self.state[1][1] and self.state[1][1] == self.state[2][2]):
            self.winner = self.state[1][1]
            self.winMethod = 'D'
            return 0
        elif(self.state[2][0] == self.state[1][1] and self.state[1][1] == self.state[0][2]):
            self.winner = self.state[1][1]
            self.winMethod = 'D'
            return 1
        return winSpot

    def checkWin(self):
        winSpot = None
        winSpot = self.checkHorizontal(winSpot)
        winSpot = self.checkVertical(winSpot)
        winSpot = self.checkDiagonal(winSpot)
        if(self.winner != None):
            self.finalizeStrings(winSpot)

    def finalizeStrings(self, winSpot):
        if(self.winner == 'X'):
            fn = redify
        elif(self.winner == 'O'):
            fn = bluify
        else:
            fn = boldify

        strings = ["","",""]

        for row in range(3):
            for col in range(3):
                strings[row] += LABEL[COORD_TO_ARRAY(row,col)] #superscript
                print(self.winMethod, row, (col + (winSpot*(2 - row))),winSpot)
                if((self.winMethod == 'H' and row == winSpot) or (self.winMethod == 'V' and col == winSpot) or (self.winMethod == 'D' and row == (col - (2*winSpot*(1 - row))))):
                    if(self.state[row][col] not in OUTPUTS):
                        strings[row] += fn("- ")
                    else:
                        strings[row] += fn(f"{self.state[row][col]} ")
                else:
                    if(self.state[row][col] not in OUTPUTS):
                        if(self.winner == False):
                            strings[row] += fn("- ")
                        else:
                            strings[row] += "- "
                    else:
                        if(self.winner == False):
                            strings[row] += fn(f"{self.state[row][col]} ")
                        else:
                            strings[row] += f"{self.state[row][col]} "
        print(strings)
        self.finalStrings = strings


    def wipe(self):
        self.state = [["a","b","c"],["d","e","f"],["g","h","i"]]

