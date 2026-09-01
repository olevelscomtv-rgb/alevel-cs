class Character:
    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed):
        self.__CharacterName = CharacterName #STRING
        self.__DateOfBirth = DateOfBirth #DATE
        self.__Intelligence = Intelligence #FLOAT
        self.__Speed = Speed #INTEGER

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, NewIntelligence):
        self.__Intelligence = NewIntelligence

    def Learn(self):
        self.__Intelligence *= 1.1

    def ReturnAge(self):
        birth_year = int(self.__DateOfBirth[:4])
        Age = 2023 - birth_year
        return Age

FirstCharacter = Character("Royal", "2019-1-19", 70, 30)
FirstCharacter.Learn()
print(f"Character Name: {FirstCharacter.GetName()}, Age: {FirstCharacter.ReturnAge()}, Intelligence: {FirstCharacter.GetIntelligence()}")
