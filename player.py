class Player(object):
    def __init__(self, type):
        self.type = type
        self.description = "Base chess player."

    def move(board):
        raise NotImplementedError("This player has no brain, and therefore no moves")