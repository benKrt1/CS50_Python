import inflect

p = inflect.engine()
names = []

def main():
    while True:
        try:
            user = input("Name: ").strip().title()
            names.append(user)
        except EOFError:
            break
    print(f"\nAdieu, adieu, to {p.join(names)}")



if __name__ == "__main__":
    main()
            