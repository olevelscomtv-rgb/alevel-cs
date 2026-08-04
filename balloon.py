# a 
class Balloon: 
    def __init__(self, DefenceItem, Colour, health=100):
        self.__DefenceItem = DefenceItem 
        self.__Colour = Colour 
        self.__health = health
    

    def GetDefenceItem(self):
        return self.__DefenceItem
    
    def ChangeHealth(self,number:int):
        self.number = number 
        self.__health += number


    def CheckHealth(self):
        if self.__health <= 0:
            return True
        else: 
            return False
    

    










if __name__ == "__main__":

    defenceItem = input("Enter the defence item\n")
    colour = input("Enter the colour\n")
    Balloon1 = Balloon(defenceItem, colour)

    def Defend(balloonObj):
        strength = int(input("Enter the strength\n"))
        balloonObj.ChangeHealth(-strength)
        print(balloonObj.GetDefenceItem())

        if balloonObj.CheckHealth():
            print("no health")
        else: 
            print("has health")

        return balloonObj




    print(Defend(Balloon1))

    

    
