def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    found_number = False

    for character in s:
        if not character.isalnum():
            return False
    if character.isdigit():
        if not found_number:
            if character == "0":
                return False
            found_number = True
    elif found_number:
        return False

    return True
       


main()


    