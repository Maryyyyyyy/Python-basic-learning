# Given code declares a player class with its attributes and an intro() method
# Complete the code to take the name and level from user input, create a player object with the corresponding values and call the intro() method of that object

class Player:
    def __init__(self,name,level):
        self.name = name
        self.level = level
    def intro(self):
        print(self.name+ "(level" + self.level + ")")

Name_input = raw_input("What is the player name?")
Level_input = raw_input("What is the level?")

Player_input = Player(str(Name_input), str(Level_input))
Player_input.intro()