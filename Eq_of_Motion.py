# Program for computing the height of a ball in vertical motion

v0 = 5      # Initial velocity (m/s)
g = 9.81    # Acceleration of gravity (m/s^2)
t = 0.6     # Time (s)

y = v0*t - 0.5*g*t**2       # Vertical position

print("Height of the ball: ", y, " m")

