"""Tar Heels exercise redux as a structured program."""

__author__ = "730393750"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))
    return None


# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(x: int) -> str:
    """Tar Heel arithmetic."""
    if x // 2 == x / 2 and x // 7 == x / 7:
        return ("TAR HEELS")
    else:
        if x // 2 == x / 2:
            return ("TAR")
        else:
            if x // 7 == x / 7:
                return ("HEELS")
            else:
                return ("CAROLINA")


if __name__ == "__main__":
    main()
