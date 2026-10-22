import sys


def main():
    file_name = check()
    count = 0
    try:
        with open(file_name) as file:
            for line in file:
                stripped = line.strip()
                if not stripped:
                    continue
                elif stripped.startswith("#"):
                    continue
                else:
                 count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)


def check():
    if len(sys.argv) > 2:
        sys.exit("Too many command-lines arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        return sys.argv[1]


if __name__ == "__main__":
    main()