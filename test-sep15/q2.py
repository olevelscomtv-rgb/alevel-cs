class Train:
    def __init__(self, TrainIDNumber, Route):
        self.__TrainIDNumber = TrainIDNumber #STRING
        self.__Route = Route #INTEGER

    def getTrainIDNumber(self):
        return self.__TrainIDNumber

    def getRoute(self):
        return self.__Route 

train1 = Train("12ADV", 134)
train2 = Train("33ART", 20)
train3 = Train("9FKF", 3)
train4 = Train("21VBC", 24)

class Station:
    def __init__(self, StationID, NumberPlatforms):
        self.__StationID = StationID #STRING
        self.__NumberPlatforms = NumberPlatforms #INTEGER
        self.__Trains = [] #LIST OF OBJECTS OF CLASS TRAIN
        self.__NumberTrains = 0 #INTEGER

    def AddTrain(self, NewTrain):
        if self.__NumberTrains >= self.__NumberPlatforms:
            return False
        else:
            self.__Trains.append(NewTrain)
            self.__NumberTrains += 1
        return True

    def GetTrain(self):
        if self.__NumberTrains == 0:
            return "There are no trains"

        line = "The trains at station " + self.__StationID + " are: \n"
    