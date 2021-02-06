"""An exercise in remainders and boolean logic."""

__author__ = "730393750"


# Begin your solution here...
integer: int = int(input("Enter an int: "))

if integer // 2 == integer / 2 and integer // 7 == integer / 7:
    print("TAR HEELS")
else:
    if integer // 2 == integer / 2:
        print("TAR")
    else:
        if integer // 7 == integer / 7:
            print("HEELS")
        else:
            print("CAROLINA")
