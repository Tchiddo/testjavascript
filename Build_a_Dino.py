# In this lab, you are the lead developer on a team building a virtual dinosaur zoo! Your task is to
# create a Python class called Dinosaur that will model different dinosaurs with attributes like
# name, species, diet, and age, and methods like roar() and eat(). You will need to create
# and test your dinosaurs by creating objects (instances) of the Dinosaur class and making them
# interact.


class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species(["Tyrannosaurus Rex", "Triceratops", "Velociraptor", "Stegosaurus"])
        self.diet
        self.age


roar = input("\nWould you like to roar? y/n ").strip()

if roar == "y":