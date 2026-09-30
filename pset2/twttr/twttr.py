user = input("Input: ").strip()

result = ""
for c in user:
    if c.lower() not in "aeiou":
        result += c

print(f"Output: {result}")
    