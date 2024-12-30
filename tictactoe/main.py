from states import *

import sys
import os

#SETUP
os.system("clear")

debug = ""

try:
    debug = sys.argv[1]
except:
    pass

inp = 'Y'
while(inp.upper() != 'N'):
    if(inp.upper() == 'Y'):
        if(debug.lower() == "debug"):
            start_game(True)
        else:
            start_game(False)
    inp = input("Play again? (Y|N): ")