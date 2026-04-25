from datetime import date
import inflect
import sys


def main():

    user_date = input("Date of Birth: ")

    if not user_date:
        sys.exit("Empty input!")

    user_convert = convert(user_date)

    minutes = convert_to_minutes(user_convert)
    print(minutes)


def convert(user_date):
    try:
        year, month, days = user_date.split("-")
    except ValueError:
        sys.exit("Invalid date!")
    try:
        year = int(year)
    except ValueError:
        sys.exit("Invalid Year!")
    try:
        month = int(month)
    except ValueError:
        sys.exit("Invalid Month!")
    try:
        days = int(days)
    except ValueError:
        sys.exit("Invalid Days!")

    today_date = date.today()

    try:
        birth = date(year, month, days)
    except ValueError:
        sys.exit("Invalid date!")

    difference = today_date - birth
    return difference.days


def convert_to_minutes(days):

    minutes = days * 24 * 60
    p = inflect.engine()
    y=p.number_to_words(minutes,andword="")
    return y.capitalize() + " minutes"


if __name__ == "__main__":
    main()
