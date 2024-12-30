class colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

LABEL = ["ᵃ","ᵇ","ᶜ","ᵈ","ᵉ","ᶠ","ᵍ","ʰ","ⁱ"]

OUTPUTS = ["X", "O"]

INPUTS = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

INPUT_MAP = {
                "a":0,
                "b":1,
                "c":2,
                "d":3,
                "e":4,
                "f":5,
                "g":6,
                "h":7,
                "i":8
            }

WIN_METHOD_STRINGS = {
    'V':"vertically",
    'H':"horizontally",
    'D':"diagonally"
}

