import random

def main():
    while True:
        try:
            user = int(input("Level: "))
            if user <= 0 :
                print("positive integer")
                pass
            else:
                break
        except ValueError:
            pass

    new_num = random.randint(1, user)

    while True:
            try:
                guess = int(input("Guess: "))
                if guess <= 0 :
                    continue
                if guess < new_num:
                    print("Too small!")
                elif guess > new_num:
                    print("Too large!")
                elif guess == new_num:
                    print("Just right!")
                    break
            except ValueError:
                pass


if __name__ == "__main__":
    main()