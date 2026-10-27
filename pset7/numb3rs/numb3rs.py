import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if match := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for num in match.groups():
            if len(num) > 1 and num.startswith("0"):
                return False
            if not 0 <= int(num) <= 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()