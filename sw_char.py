character_name = input ("What is the name of your character?")
species = input ("What species is your character?")
occupation = input ("What is your character's occupation? (e.g., Jedi, Sith, Smuggler)")
weapon = input ("What main weapon wil your character weild?")
home_planet = input ("What planet does your character originate from?")
import random

sidekicks = ["R2-D2", "Chewbacca", "BB-8", "K-250", "C-3PO"]
sidekick = random.choice(sidekicks)


print ("/n--------------- STAR WARS CHARACTER BIO --------------------")
print (f"Name: {character_name}")
print (f"Species: {species}")
print (f"Occupation: {occupation}")
print (f"Weapon: {weapon}")
print (f"Home Planet: {home_planet}")
print (f"Sidekick: {sidekick}")
print ("------------------------------------------------------------/n")

if occupation== "sith":
    print(f"{character_name} is a Sith. Your loyalty to greatness is recognized")
elif occupation  == "jedi" :
    print (f"{character_name} is a Jedi. You disgust me, and the rest of the empire")
else :
    print (occupation)
