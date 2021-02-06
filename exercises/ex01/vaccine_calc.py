"""A vaccination calculator."""

__author__ = "730393750"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target: int = int(input("Target percent vaccinated: "))

time_required: float = (2 * population * (target / 100) - doses_admin) / doses_per_day

today: datetime = datetime.today()
days_until_target: timedelta = timedelta(round(time_required))
date_of_target: datetime = today + days_until_target
target_date: str = date_of_target.strftime("%B %d, %Y")

print("We will reach " + str(target) + "% vaccination in " + str(round(time_required)) + " days, which falls on " + target_date + ".")
