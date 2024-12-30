from Board import *

class MegaBoard:
    def __init__(self):
        self.state = [[Board(),Board(),Board()],[Board(),Board(),Board()],[Board(),Board(),Board()]]

    def __str__(self):
        return f"{self.state}"