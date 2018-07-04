import random

print("Rolling the dice...")
dice1 = random.randint(1, 6)
print("Die 1: %d" % dice1)
dice2 = random.randint(1, 6)
print("Die 2: %d" % dice2)
print("Total value: %d" % (dice1 + dice2))
