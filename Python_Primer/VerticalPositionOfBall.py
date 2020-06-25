# Program for computing the vertical position of a ball
initial_velocity = 5
acceleration_of_gravity = 9.81
TIME = 0.6
VerticalPositionOfBall = initial_velocity * TIME - 0.5 * acceleration_of_gravity * TIME ** 2
print("Vertical Position Of Ball = ", VerticalPositionOfBall)