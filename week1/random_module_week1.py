import random

prob = random.random()# return floats between 0 and 1
print(prob)

diceThrow = random.randrange(1,7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)

######

from random import random, randrange
prob = random()
print(prob)
diceThrow = randrange(1,7)
print(diceThrow)