user = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

match user.lower().replace(" ", "").replace("-",""):
    case "42" | "fortytwo":
        print("Yes")
    case _:
        print("No")