from items import *
from locations import *
from res.character import Character
from res.game import Game

g = Game()
g.character = Character()


name = ""
while name == "":
    name = input("What is your name, brave adventurer: ")

g.character.name = name
g.character.location = farmstead
g.character.weapon = blunt_rock
g.character.armour = farming_clothes

g.printintro()

# test code
# print(g.character.location.name)
# end test
g.playing = True

while g.playing:
    # Play the game!
    # Repeating effects (poison, day and night, etc...)
    print(g.endofturn_step())
    # Print location introduction (if printing here, do not print on arrival)

    # Get input from player
    print(g.process_command(input(">>> ")))


input("Enter to Exit...")
