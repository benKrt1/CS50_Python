user = input("Expression: ").strip().split(" ")

x = float(user[0])
y = user[1]
z = float(user[2])

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    pass
