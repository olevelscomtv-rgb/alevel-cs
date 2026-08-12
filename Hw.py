class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number
        self.__Colour = Colour

    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour

r1 = Card(1, 'red')
r2 = Card(2, 'red')
r3 = Card(3, 'red')
r4 = Card(4, 'red')
r5 = Card(5, 'red')

b1 = Card(1, 'blue')
b2 = Card(2, 'blue')
b3 = Card(3, 'blue')
b4 = Card(4, 'blue')
b5 = Card(5, 'blue')

y1 = Card(1, 'yellow')
y2 = Card(2, 'yellow')
y3 = Card(3, 'yellow')
y4 = Card(4, 'yellow')
y5 = Card(5, 'yellow')

class Hand:
    def __init__(self, C1, C2, C3, C4, C5):
        self.C1 = Card(C1)
        self.C2 = Card(C2)
        self.C3 = Card(C3)
        self.C4 = Card(C4)
        self.C5 = Card(C5)
        self.FirstCard = 0
        self.NumberCards = 5
