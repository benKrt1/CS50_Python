def main():
    dollars = dollars_to_float("How much was the meal? ")
    percent = percent_to_float("What percentage would you like to tip? ")
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    price = input(d)
    pri = price.strip("$")
    return float(pri)


def percent_to_float(p):
    percent = input(p)
    per = percent.strip("%")
    flo = float(per) / 100
    return flo


main()