"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730393750"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    date: str = future_date(days)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + date + ".")


# TODO 1: Define days_to_target function
def days_to_target(w: int, x: int, y: int, z: int) -> int:
    time_required: float = (2 * w * (z / 100) - x) / y
    return int(round(time_required))


# TODO 3: Define future_date function
def future_date(x: int) -> str:
    today: datetime = datetime.today()
    days_to_go: timedelta = timedelta(round(x))
    day_of_target: datetime = today + days_to_go
    return str(day_of_target.strftime("%B %d, %Y"))


if __name__ == "__main__":
    main()
