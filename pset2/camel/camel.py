camel = input("camelCase: ").strip()

result = ""
for c in camel:
    if c.isupper():
        result += "_" + c.lower()
    else:
        result += c

print(f"snake_case {result}")