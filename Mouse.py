"""
    Mouse movement
"""
import random as rnd
class Maze:
    direction = -1  # set at -1 to get the loop going
    maze = []
    # attributes
    def __init__(self, steps = 0):
        self.steps = steps
    # methods
    def create_maze(self):
        print("Create the maze for the mouse.")
        while self.steps <= 0 or type(self.steps) != int:
            try:
                self.steps = int(input("How many steps does your maze have?\n"))
            except ValueError:
                print("Buzzer! Sorry, you failed to enter a positive integer\n or your number is 0.")
        print()
        for i in range(0,self.steps):
            print("Which way should the mouse move to complete step " + str(i+1) + "?")
            print("0 = forward, 1 = left, 2 = right")
            while self.direction < 0 or self.direction > 2 or type(self.direction) != int:
                try:
                    self.direction = int(input("Make your selection:\n"))
                except ValueError:
                    print("What is your problem? Enter 0, 1, or 2?")
            self.maze.append(self.direction)
            self.direction = -1 # reset
    def display_maze(self):
        s = "To get the cheeze, the mouse go\n"
        for i in range(0,self.steps):
            if self.maze[i] == 0:
                s += "forward, "
            elif self.maze[i] == 1:
                s += "left, "
            else:
                s += "right, "
            if i > 4 and i % 5 == 0:
                s += "\n"
        print(s)
        input("Press enter to continue ...")
    def which_way(self,maz):
        if maz == 0:
            s = "forward"
        elif maz == 1:
            s = "left"
        else:
            s = "right"
        return s
    @staticmethod
    def timer():    # slow the display pace
        x = 0
        while x < 4000000:
            x += 1

class Mouse:
    def __init__(self):
        self.status = [0,0,0]   # the status of each direction is zero
        self.numerator = [1,1,1]    # for weights
        self.denominator = [1,1,1]  # for weights
    # methods:
    def get_rnd_number(self):
        roll = rnd.randint(0,2)
        return roll
g0 = "Mouse moves forward"
g1 = "Mouse moves left"
g2 = "Mouse moves right"
b0 = "Mouse hits a brick wall!"
b2 = "Electric mousetrap fries mouse!"
good_