# Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system. Remember, the force of gravity is different on each planet, so your weight will be different for each planet. 

print ("---------------------------------------")
print (" ")

print ("Little Codey! We've heard so much about you! Please select your current weight, then, your planet your next fight is on so we can idenify your weight! ") 

print (" ")

weight = float(input ("Enter weight: "))

print ("   0. Mercury  1. Venus   2. Mars    ")
print ("   3. Jupiter  4. Saturn  5. Uranus  ")
print ("     6. Neptune          7. Pluto    ")

print (" ")

print ("Of our seven options, please select the nuumber of your planet! (ex: 0, 4, 6)")

planet = input ("Enter planet here: ")


planets = {
    "0": {"name": "Mercury", "factor": 0.90},
    "1": {"name": "Venus", "factor": 0.91},
    "2": {"name": "Mars", "factor": 0.38},
    "3": {"name": "Jupiter", "factor": 2.34},
    "4": {"name": "Saturn", "factor": 1.06},
    "5": {"name": "Uranus", "factor": 0.92},
    "6": {"name": "Neptune", "factor": 1.19},
    "7": {"name": "Pluto", "factor": 0.063}
}


print (" ")
print ("---------------------------------------")
print(" ")


if planet in planets:
    planet_info = planets[planet]
    new_weight = weight * planet_info["factor"]
    print(f"Your weight on {planet_info['name']} will be {new_weight:.2f}")

else:
    print("Sorry, that's not a valid planet number!")
print(" ")
