def OutputItem():
    animal = Animal.pop()
    colour - Colour.pop()

    if animal == None and colour != None:
        Animal.push(animal)
        print("No colour")

    elif animal != None and colour == None:
        Colour.push(colour)
        print("No animal") 

    else:
        print(f"{colour} {animal}")