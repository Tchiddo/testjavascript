import random

name = "Josh"
question = "Will I ever be rich?"
answer = ""

random_number = random.randint(1, 11)

if random_number == 1:
  answer = "Yes - definitely"

elif random_number == 2:
    answer = "It is decidedly so"

elif random_number == 3:
    answer = "Without a doubt"

elif random_number == 4:
    answer = "Reply hazy, try again"

elif random_number == 5:
    answer = "Ask again later"

elif random_number == 6:
    answer = "Better not tell you now"

elif random_number == 7:
    answer = "My sources say no"

elif random_number == 8:
    answer = "Outlook not so good"

elif random_number == 9:
    answer = "Very doubtful"
    
elif random_number == 10:
    answer = "Not a chance buddy"

elif random_number == 11:
    answer = "Don't even think about it"

else: 
  answer = "Error"
#To check if the name is not given
if name == "":
  print (question)

else:
  print (name, "asks", question) 
  #To check if the question is not given
if question == "":
  print ("Sorry, I didn't hear you")

else:
  print ("Magic 8-Ball's answer:", answer)

