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

class MagicCharacter(Character):
    def __init__(self, Element, CharacterName, DateOfBirth, Intelligence, Speed):
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.__Element = Element #STRING

    def Learn(self):
        if self.__Element == "Fire" or self.__Element == "Water":
            self.SetIntelligence(self.GetIntelligence() * 1.2)
        elif self.__Element == "Earth":
            self.SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            self.SetIntelligence(self.GetIntelligence() * 1.1)

FirstMagic = MagicCharacter("Fire", "Light", "2018-3-3", 75, 22)
FirstMagic.Learn()
print(f"Character Name: {FirstMagic.GetName()}, Age: {FirstMagic.ReturnAge()}, Intelligence: {FirstMagic.GetIntelligence()}")