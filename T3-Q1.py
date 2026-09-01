StackVowel = ['']*100
StackConsonant = ['']*100
VowelTop = 0
ConsonantTop = 0

def PushData(letter):
    global VowelTop, ConsonantTop, StackVowel, StackConsonant

    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        if VowelTop == 100:
            print("Vowel stack is full!")
        else:
            StackVowel[VowelTop] = letter
            VowelTop += 1
    else:
        if ConsonantTop == 100:
            print("Consonant stack is full!")
        else:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop += 1

def ReadData():

    try:
        file = open("StackData.txt", "r")
        for i in file:
            letter = i
            if letter != "":
                PushData(letter)
        file.close()
    except FileNotFoundError:
        print("File not found!")

def PopVowel():
    global VowelTop, StackVowel
    if VowelTop == 0:
        print("Vowel stack is empty!")
        return "No data"
    else:
        VowelTop -= 1
        return StackVowel[VowelTop]

def PopConsonant():
    global ConsonantTop, StackConsonant
    if ConsonantTop == 0:
        print("Consonant stack is empty!")
        return "No data"
    else:
        ConsonantTop -= 1
        return StackConsonant[ConsonantTop]
        
if __name__ == "__main__":
    ReadData()
    returned_letters = []
    
    while len(returned_letters) < 5:
        choice = input("Enter 'vowel' to pop a vowel or 'consonant' to pop a consonant: ")
        
        if choice.lower() == "vowel":
            result = PopVowel()
            if result != "No data":
                returned_letters.append(result)
        elif choice.lower() == "consonant":
            result = PopConsonant()
            if result != "No data":
                returned_letters.append(result)
        else:
            print("Invalid choice, please enter 'vowel' or 'consonant'.")