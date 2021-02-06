"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730393750"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

fortune: int = randint(1, 4)

if fortune == 1:
    print("Love is headed your way!")
else:
    if fortune == 2:
        print("Your hard work will pay off soon!")
    else:
        if fortune == 3:
            print("A pleasant surprise is in store for you this week!")
        else:
            if fortune == 4:
                print("Tomorrow will be a great day to try something new!")

print("Now, go spread positive vibes!")
