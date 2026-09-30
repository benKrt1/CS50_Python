def meow(n: int) -> str:
    """
    Meow n time.

    :param n: Number of time to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n
    #to "None" einai gia to mypy pou leei oti den prepi na giziri
    #"None" opos kani me to line meows: str = meow(number)
    #for _ in range(n):
       # print("meow")

#trexo to mypy meows2.py gia na kanis to test
#to "number: int" einai san tag pou leei sto programa/mypy 
#oti auto prepi na einai int
number: int = int(input("Number:"))
# i ano kato telia einai san tag
meows: str = meow(number)
"""" 
o sostos gia na kanis documetetion einai tria monis/diples ano telies
"""
print(meows, end="")


