class Excercise:
    def __init__(self, ExerciseType: str, Duration: int, CaloriesBurned: float = 0):
        self.__ExerciseType = ExerciseType
        self.__Duration = Duration
        self.__CaloriesBurned = CaloriesBurned


    def GetExerciseType(self):
        return self.__ExerciseType
    
    def GetDuration(self):
        return self.__Duration
    
    def GetCaloriesBurned(self):
        return self.__CaloriesBurned

    def CalculateCalories(self, ExerciseType, Duration):
        if self.__ExerciseType == 'Running':
            self.__CaloriesBurned = self.__Duration * 10
        elif self.__ExerciseType == 'Swimming':
            self.__CaloriesBurned = self.__Duration * 8
        elif self.__ExerciseType == 'Walking':
            self.__CaloriesBurned = self.__Duration * 5
        else:
            self.__CaloriesBurned = self.__Duration * 6