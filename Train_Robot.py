"""
    This program trains a robot to
    rotate left and right, up and down
    over a distance within a time period.
"""
# Author: GM Jackson

class Robot(object):
    def __init__(self):
        self.file_name = ""
        self.real = [0,0,0,0]
        self.param = ""
        self.file_str = ""
        self.answer = 0
        self.inc = 0
        self.theta = 0
        self.count = 0
        self.chosen = 1000000000
        self.chosen_theta = 0
        self.ini_theta = [-10,10]
    def get_file_name(self):
        self.file_name = input("To save move results, choose a file name:\n")
    def train_robot_moves(self):
        for i in range(0,len(self.real)):
            if i == 0:
                self.real[i] = float(input("Enter a left-right rotation angle:\n"))
                self.param = "left-right rotation"
            elif i == 1:
                self.real[i] = float(input("Enter an up-down rotation angle:\n"))
                self.param = "up-down rotation"
            elif i == 2:
                self.real[i] = float(input("Enter an up-down rotation angle:\n"))
                self.param = "up-down rotation"
            else:
                self.real[i] = float(input("Enter a time period:\n"))
                self.param = "time"
            self.file_str = ""
            self.answer = 0
            self.inc = 0
            self.theta = 0
            self.count = 0
            self.chosen = 1000000000
            self.chosen_theta = 0
            for j in range(0,len(self.ini_theta)):
                self.answer = abs(self.ini_theta[j] - self.real[i])
                if self.answer <= self.chosen:
                    self.chosen = self.answer
                    self.chosen_theta = self.ini_theta[j]
            self.inc = self.chosen_theta
            self.theta = self.chosen_theta
            while self.answer > .01 and self.count < 1000:
                self.theta += self.inc
                self.count += 1
                self.answer = abs(self.theta - self.real[i])
                if self.answer <= self.chosen:
                    self.chosen = self.answer
                    self.chosen_theta = self.theta
                else:
                    if abs(self.theta - 2*self.inc) > 0:
                        self.theta -= 2*self.inc
                    else:
                        self.theta = 0

                        self.inc /= 10
                        self.chosen = 1000000000    # reset to prevent stuck near 0
                    self.file_str = str(self.count) + ": " + self.param + " = " + str(self.real[i]) + self.param + " = " + str(round(self.chosen_theta,2)) + "\n"
                    print(self.file_str)
                    with open(self.file_name + '.txt', 'a', encoding = 'utf-8') as Hal9000:
                        Hal9000.write(self.file_str)
# end Robot class /////////////////////////////////////////////////////////////////////////////////////////////////
# Begin program:
robot = []
# get the moves down:
moves = int(input("Enter the number of robot moves:\n"))
for i in range(0,moves):
    robot.append(Robot())
# Train the robot:
for i in range(0,moves):
    robot[i].get_file_name()
    # refine robot's moves and record data:
    robot[i].train_robot_moves()