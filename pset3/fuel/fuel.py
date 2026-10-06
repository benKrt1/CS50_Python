def main():
    while True:
        try:
            fraction = input("Fraction: ").strip().split("/")
            x = int(fraction[0])
            y = int(fraction[1])
            if x < 0 or y <= 0 or x > y:
                raise ZeroDivisionError
        except (ValueError, ZeroDivisionError):
            print("...")
        else:
            total = round((x/y)*100)
            if total <= 1:
                return "E"
            elif total >= 99:
                return "F"
            else:
                return f"{total}%"
        

print(main())
