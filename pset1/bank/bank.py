user = input("Greeting: ").lstrip().strip().lower()

hello = user.startswith("hello")
h = user.startswith("h")


if hello:
    print("$0")
elif h:
    print("$20")
else:
    print("$100")



