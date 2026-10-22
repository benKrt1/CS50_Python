def main():
    user = input("Input: ").strip()
    result = shorten(user)
    print(f"Output: {result}")


def shorten(word):
    result = ""
    for c in word:
        if c.lower() not in "aeiou":
            result += c
    return result

if __name__ == "__main__":
    main()
    