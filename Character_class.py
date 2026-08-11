class Character:
    def __init__(self, Name, XCoordinate, YCoordinate): #(Name: str, XCoordinate: int, YCoordinate: int)
        self.__Name = Name
        self.__XCoordinate = XCoordinate
        self.__YCoordinate = YCoordinate

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange
