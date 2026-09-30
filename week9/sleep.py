def main():
    n = int(input("What's is n?"))
    for s in sheep(n):
        #print("SheP" * i)
        print(s)

def sheep(n):
    for i in range(n):
        yield "SheeP" * i

if __name__ == "__main__":
    main()

