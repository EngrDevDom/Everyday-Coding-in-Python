# Program for computing the height of a ball in vertical motion
v0 = 5      # initial velocity
g = 9.81    # acceleration of gravity
t = 0.6     # time
y = v0*t - 0.5*g*t**2   # vertical position
print('1st comment: ', 'At t = %g s, the height of the ball is %.2f m.' % (t, y))
print('2nd comment: ', 'At t = %f s, a ball with initial velocity'
                       ' v0 = %.3E m/s is located at the height %.2f m.' % (t, v0, y))