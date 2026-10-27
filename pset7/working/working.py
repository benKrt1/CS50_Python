import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)",
        s,
    )
    if not match:
        raise ValueError

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = (
        match.groups()
    )
    start = to24hour(start_hour, start_minute, start_period)
    end = to24hour(end_hour, end_minute, end_period)
    return f"{start} to {end}"


def to24hour(hour, minute, period):
    hour = int(hour)
    minute = 0 if minute is None else int(minute)

    if not 1 <= hour <= 12 or not 0 <= minute <= 59:
        raise ValueError

    if period == "AM":
        hour = 0 if hour == 12 else hour
    elif hour != 12:
        hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
