class Excercise:
    def __init__(self, ExerciseType: str, Duration: int, CaloriesBurned: float = 0):
        self.__ExerciseType = ExerciseType
        self.__Duration = Duration
        self.__CaloriesBurned = CaloriesBurned


    def GetExerciseType(self):
        return f'Exercise: {self.__ExerciseType}'
    
    def GetDuration(self):
        return self.__Duration
    
    def GetCaloriesBurned(self):
        return f'Calories Burned: {self.__CaloriesBurned}'

    def CalculateCalories(self, ExerciseType, Duration):
        if self.__ExerciseType == 'Running':
            self.__CaloriesBurned = self.__Duration * 10
        elif self.__ExerciseType == 'Swimming':
            self.__CaloriesBurned = self.__Duration * 8
        elif self.__ExerciseType == 'Walking':
            self.__CaloriesBurned = self.__Duration * 5
        else:
            self.__CaloriesBurned = self.__Duration * 6

def Exercise_Machine():
    print('Available Exercises: Running, Swimming, Walking, Other.')
    exercise = input('Please enter the choosen exercise: ')
    Valid_time = False
    while Valid_time == False:
        time = int(input('Please enter the time (1-300min): '))
        if time < 1 or time > 300:
            print("Not Valid")
        else:
            Valid_time = True

    e1 = Excercise(exercise, time)
    e1.CalculateCalories(exercise, time)
    print(e1.GetExerciseType())
    print(e1.GetCaloriesBurned())

Exercise_Machine()