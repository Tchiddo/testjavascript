# Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system. Remember, the force of gravity is different on each planet, so your weight will be different for each planet. 

print ("---------------------------------------")
print (" ")

print ("welcome space cowpoke! Before we shoot you off to space, we need to know your current earth weight, and what planet you'll be sent to, so we can correctly idenify your weight on that planet!") 

print (" ")

weight = float(input ("Enter weight: "))

print ("   0. Mercury  1. Venus   2. Mars    ")
print ("   3. Jupiter  4. Saturn  5. Uranus  ")
print ("     6. Neptune          7. Pluto    ")

print (" ")

print ("Of our six options, please select the nuumber of your planet so we can correctly idenify your weight! (ex: 0, 4, 6)")

planet = input ("Enter planet here: ")

print (" ")
print ("---------------------------------------")


if planet == "0":
  print (f"Your weight on Mercury will be {weight * 0.90} ")

elif planet == "1":
  print (f"Your weight on Venus will be {weight * 0.91} ")

elif planet == "2":
  print (f"Your weight on Mars will be {weight * 0.38} ")

elif planet == "3":
  print (f"Your weight on Jupiter will be {weight * 2.34} ") 

elif planet == "4":
  print (f"Your weight on Saturn will be {weight * 1.06} ") 

elif planet == "5":
  print (f"Your weight on Uranus will be {weight * 0.92} ")

elif planet == "6":
  print (f"Your weight on Neptune will be {weight * 1.19} ") 

elif planet == "7":
  print (f"Your weight on Pluto will be {weight * 0.063} ") 

  print (" ")
