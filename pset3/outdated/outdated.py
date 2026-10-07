months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user = input("Date: ").strip()
    if "/" in user:
        mdy = user.split("/")
        if len(mdy) == 3:
            try:
                m = int(mdy[0])
                d = int(mdy[1])
                y = int(mdy[2])
                if m >= 1 and m <= 12 and d >= 1 and d <= 31:
                    print(f"{y:04d}-{m:02d}-{d:02d}")
                    break
            except ValueError:
                pass
    elif "," in user:
        first, year_part = user.split(",")
        words = first.split()
        if len(words) == 2:
            month = words[0].title()
            day = words[1]
            if month in months:
                try:
                    month = months.index(month) + 1
                    day = int(day)
                    year = int(year_part.strip())
                    if month >= 1 and month <= 12 and day >= 1 and day <= 31:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
                except ValueError:
                    pass