"""Examples using loops."""

count: int = 0
while input("Do you need more love? yes/no - ") == "yes":
    # Body block of the while loop is evaluated
    # when the test expression is true
    print("I love you!")
    count += 1
    print(f"Count is {count}.")


# Iterating a specific number of times
i: int = 0 # i is typically short for index
iterations: int = 10

while i < iterations:
    print(f"I love you! i: {i}")
    i += 1


print("Have a lovely day!")
