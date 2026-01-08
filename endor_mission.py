# Simms, Jayden
import datetime
import random

squads = {"Red Squad", "Blue Squad", "Gold Squad"}

print("\nBeginning mission in 3..2..1..")
input("\nType anything to start: ")
print(
    "\nGeneral, we need your help. Our squads are in total shambles. Our assult on the second death start wil falter if we dont get our bearings quick!"
)
input("\nType anything to continue: ")

print(
    f"\nWe currently have 3 squads available for guidance! How many squads can you take under your wing?"
)

squad_guide = {"Red Squad", "Gold Squad", "Green Squad"}

print("\nEnter how many squads you would like to command ")
squad_input = int(input("\nSelect 1, 2, or 3: ").strip())

if squad_input == 1:
    print(f"\nOkay, 1. We can work with that. Assigning you the Red Squad ")
    input("\nType anything to continue: ")

elif squad_input == 2:
    print(f"\nOkay, 2. We can work with that. Assigning you the Red and Gold Squads ")
    input("\nType anything to continue: ")

elif squad_input == 3:
    print(
        f"\nOkay, 3. We can work with that. Assigning you the Red, Gold, and Green squads "
    )
    input("\nType anything to continue: ")

else:
    print(
        "\nWhat are you talking about? I said 1, 2, or 3. Terminating job for your ignorance."
    )

# Yo sekol I am actually cooked. Don't tell me im gonna have to.. s s s s s STUDY!??
