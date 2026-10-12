import sys
import random

from pyfiglet import Figlet


figlet = Figlet()


if len(sys.argv) == 1:
    f_style = random.choice(figlet.getFonts())
    figlet.setFont(font=f_style)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Invalid font")
        figlet.setFont(font=font)
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


user = input("Input: ")
print(figlet.renderText(user))
