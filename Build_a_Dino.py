# In this lab, you are the lead developer on a team building a virtual dinosaur zoo!
# Your task is to create a Python class called Dinosaur that will model different dinosaurs
# with attributes like name, species, diet, and age, and methods like roar(), eat(), and dino_info().
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

    def eat(self, food):
        if food.lower() in [item.lower() for item in self.diet]:
            print(f"{self.name} the {self.species} happily eats the {food}.")
        else:
            print(f"{self.name} the {self.species} refuses to eat {food}!")

    def dino_info(self):
        # Join all diet items into a readable list string
        diet_list = ", ".join(
            self.diet
        )  # .join gets rid of the quotation marks and brackets that would show if you just printed diet_list normally
        return f"Name: {self.name}, Species: {self.species}, Diet: {diet_list}, Age: {self.age}"


# Create dinosaur instances
dino1 = Dinosaur(
    "Sekol", "Triceratops", ["fruits", "seeds", "leaves", "twigs", "roots"], 30
)
dino2 = Dinosaur("Freyn", "Velociraptor", ["lizards", "dino eggs", "a baby dino"], 10)
dino3 = Dinosaur(
    "Simms", "Stegosaurus", ["mosses", "ferns", "horsetails", "cycads"], 17
)

dino1.roar()
dino2.eat("lizards")
dino3.eat("meat")

print(" ")
print(dino1.dino_info())
print(dino2.dino_info())
print(dino3.dino_info())
