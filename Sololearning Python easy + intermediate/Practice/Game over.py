# Given code declares a player class with its attributes and an intro() method
# Complete the code to take the name and level from user input, create a player object with the corresponding values and call the intro() method of that object

class Player:
    def __init__(self,name:str,level):
        #Validation to receive argument
        # if values is used here, we can use assert argument to rule out value that is not in expectation
        # assert level >=0, f"level {level} is not greater or equal to zero" 
        # if the input level is smaller than 0, it will run as assertionerror "level is not greater or equal to zero"
        #Assign to self object
        self.name = name
        self.level = level
    def intro(self):
        print(self.name+ "(level" + self.level + ")")

Name_input = raw_input("What is the player name?")
Level_input = raw_input("What is the level?")

Player_input = Player(str(Name_input), str(Level_input))
Player_input.intro()