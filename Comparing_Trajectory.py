'''
    Drawing the trajectory of a body in Projectile Motion
    Then comparing the trajectory to 3 velocities
'''

from matplotlib import pyplot as plt
import math

# Label the Graph
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a Ball')

# Define the Range
def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start += interval
    return numbers

# Draw the Trajectory
def draw_trajectory(u, theta):
    # Convert the angle to radians
    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2*u*math.sin(theta)/g

    # Find time intervals
    intervals = frange(0, t_flight, 0.001)

    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t)

    draw_graph(x, y)

# This is the main program
if __name__ == '__main__':

    # List of three initial velocities
    u_list = [20, 40, 60]
    theta = 45
    for u in list:
        draw_trajectory(u, theta)

    # Add a legend and show the graph
    plt.legend(['20', '40', '60'])
    plt.show()

