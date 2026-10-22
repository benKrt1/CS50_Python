import sys
import csv


def main():
    read()
    write()


students = []

def read():
    csv_file = check_file()
    try:
        with open(csv_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                students.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {csv_file}")
    return students


def write():
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


def check_file():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]


if __name__ == "__main__":
    main()