import emoji


def main():
    user = input("Input: ").strip()
    print(emoji.emojize(f"Output: {user}", language='alias'))

if __name__ == "__main__":
    main()
