def main():
    items = {}
    while True:
        try:
            user = input().strip().upper()
            if user:
                items[user] = items.get(user, 0) + 1
        except EOFError:
            print()
            break
    for user in sorted(items.keys()):
        print(f"{items[user]} {user}")


if __name__ == "__main__":
    main()

