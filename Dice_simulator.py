import random
random.seed(100)

for roll in range(10):
      print(random.randint(1,6))

print("Re-seeded")
random.seed(100)

for roll in range(10):
      print(random.randint(1,6))
