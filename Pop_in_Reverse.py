import random
import time

start_time = time.time()        # Initialize start time

Stack = []          # Stack 1
revStack = []       # Stack 2

input("\nPress ENTER to start!")

# Loops through stack and adds integer until max length
for i in range(0, 1000):
    i = (random.randint(0, 1000000))
    print("Stack value: ", i)
    Stack.append(i)

print("")
input("\nPress ENTER to pop in reverse!")
print("")

# Pops through stack in reverse
for i in range(0, 1000):
    i = Stack.pop(-1)
    print("revStack value: ", i)
    revStack.append(i)

end_time = time.time()      # Initialize end time

# Calculate total time
total_time = int(end_time - start_time)

print("\nYou waited [", round(total_time, 8), "] seconds.")     # print in seconds
print("or ", round(total_time / 60, 2), " minutes.")            # print in minutes

