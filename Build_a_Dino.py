# In this lab, you are the lead developer on a team building a virtual dinosaur zoo!
# Your task is to create a Python class called Dinosaur that will model different dinosaurs
# with attributes like name, species, diet, and age, and methods like roar() and eat().
# You will need to create and test your dinosaurs by creating objects (instances) of the Dinosaur class
# and making them interact.


class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age

    def roar(self):
        print(f"{self.name} the {self.species} lets out a mighty ROAR!")


# Create dinosaur instances
dino1 = Dinosaur(
    "Sekol", "Triceratops", ["fruits", "seeds", "leaves", "twigs", "roots"], 30
)
dino2 = Dinosaur("Freyn", "Velociraptor", ["lizards", "dino eggs", "a baby dino"], 10)
dino3 = Dinosaur(
    "Simms", "Stegosaurus", ["mosses", "ferns", "horsetails", "cycads"], 17
)

# Example of interaction
dino1.roar()
dino2.roar()
dino3.roar()
