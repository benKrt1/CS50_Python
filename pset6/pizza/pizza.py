import sys
from tabulate import tabulate
import csv

menu = []

def main():
    csv_file = check_csv()
    try:
        with open(csv_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)
        print(tabulate(menu, headers="keys", tablefmt="grid"))       
    except FileNotFoundError:
        sys.exit(f"Could not read{sys.argv[1]}")

    


def check_csv():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]


if __name__ == "__main__":
    main()