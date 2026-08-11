class Excercise:
    def __init__(self, ExerciseType: str, Duration: int, CaloriesBurned: float):
        self.__ExerciseType = ExerciseType
        self.__Duration = Duration
        self.__CaloriesBurned = CaloriesBurned

    def Constructor(self, ExerciseType, Duration, CaloriesBurned = 0):
        pass
    def GetExerciseType(self):
        return self.__ExerciseType
    def GetDuration(self):
        return self.__Duration
    def GetCaloriesBurned(self):
        return self.__CaloriesBurned