class House:

    def __init__(self, x, y):
        self.nbvisits = 0
        self.x = x
        self.y = y

    def Visit(self):
        self.nbvisits = self.nbvisits + 1

    def GetCoordinates(self):
        return [self.x, self.y]

