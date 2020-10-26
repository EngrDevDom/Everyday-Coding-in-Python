import sys

number = input("Please enter a number:" + "\n" + ">>> ")
number = int(number)
prime = False   # Initiate boolean for true false, default false

if number > 0:
    for x in range(2, number - 1):  # this range excludes number and 1, both of which number
                                    # is divisible

        # If number isn't evenly divisible by x, start over with the next one
        if number % x != 0:
            continue

        # If number is evenly divisible by x, it can't be prime
        elif number % x == 0:
            sys.exit("The number is not prime.")

    sys.exit("The number is prime.")    # number wasn't evenly divisible by x, so it's prime

# Considering that 0 is not prime
elif number == 0:
    sys.exit("The number is not prime.")

# If number is less than 0, consider the number is not prime
else:
    sys.exit("The number is not prime.")

