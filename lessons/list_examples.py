"""Some examples of list concepts."""

rolls: list[int] # Declare a variable whose type is a list of ints

rolls = [2, 3, 2, 6] # Initialize w/ list literal syntax

print(f"Length of rolls is {len(rolls)}")

from random import randint
rolls.append(randint(1, 6)) # List's append method adds an item to the end of a list
print(rolls)

rolls.pop() # List's pop method, with no argument, removes the last item of a list
print(rolls)