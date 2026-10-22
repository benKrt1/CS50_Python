def main():
    user = input("Greeting: ")
    print(value(user))
    


def value(greeting):
    user = greeting.strip().lower()
    hello = user.startswith("hello")
    h = user.startswith("h")


    if hello:
        return int(0)
    elif h:
        return int(20)
    else:
        return int(100)

    return value()

if __name__ == "__main__":
    main()
