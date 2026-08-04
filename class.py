# creating Lesson class
class Lesson:
    def __init__(self, LessonType, Instructor):
        self.__LessonType = LessonType
        self.__Instructor = Instructor

    def GetLessonType(self):
        return self.__LessonType

    def GetFree(character):
        if character == "B":
            return "$45"
        elif character == "I":
            return "$50"
        elif character == "A":
            return "$55"
        else:
            return -1

# creating array of lessons

LessonArray = [' '] * 3

# it is 9 not 3 
LessonArray = [' '] * 9

LessonArray[2] = Lesson("Improve Your Serve", "David")



print(LessonArray)

