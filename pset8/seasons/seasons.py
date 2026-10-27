import sys
from datetime import date

import inflect


def main():
    try:
        birthday = parse_date(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    minutes = age_in_minutes(birthday, date.today())
    print(f"{minutes_to_words(minutes)} minutes")


def parse_date(s):
    if len(s) != 10 or s[4] != "-" or s[7] != "-":
        raise ValueError
    return date.fromisoformat(s)


def age_in_minutes(birthday, today):
    return (today - birthday).days * 24 * 60


def minutes_to_words(minutes):
    engine = inflect.engine()
    return engine.number_to_words(minutes, andword="").capitalize()


if __name__ == "__main__":
    main()