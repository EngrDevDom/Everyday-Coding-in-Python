# File  :   cball3.py
# Desc  :

from math import sin, cos, radians

class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        return self.ypos

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

def getInputs():
    angle = float(input("Enter the launch angle (in degrees): >> "))
    vel = float(input("Enter the initial velocity (in meters/sec): >> "))
    h0 = float(input("Enter the initial height (in meters): >> "))
    time = float(input("Enter the time interval between position calculations: >> "))
    return angle, vel, h0, time

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)

    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

main()
