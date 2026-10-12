import random


def main():
    level = get_level()
    answer = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y

        for _ in range(3):
            try:
                user = int(input(f"{x} + {y} = "))
                if user == z:
                    answer += 1
                    break
                print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {z}")

    print(f"Score: {answer}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                pass
            else:
                continue
            return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    elif level == 3:
        n = random.randint(100 , 999)
    else:
        raise ValueError

    return n


if __name__ == "__main__":
    main()
