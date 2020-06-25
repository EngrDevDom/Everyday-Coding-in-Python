# This program identifies what type of triangle it is
# based on the measure of it's angle

angle = int(input("Give an angle in degrees: "))
type = ""

if angle > 0 and angle < 90:
    type = "ACUTE"
elif angle == 90:
    type = "RIGHT"
elif angle > 90 and angle < 180:
    type = "OBTUSE"
elif angle == 180:
    type = "STRAIGHT"
elif angle > 180 and angle < 360:
    type = "REFLEX"
elif angle == 360:
    type = "COMPLETE"
else:
    type = "UNIDENTIFIED"

print("The triangle is a/an: ", type)