import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """Return a shareable URL for a YouTube video embedded in HTML."""
    match = re.search(
        r'<iframe[^>]*\bsrc="https?://(?:www\.)?youtube\.com/embed/([^"?]+)',
        s,
    )
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()