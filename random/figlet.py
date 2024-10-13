from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) == 1:
    x = input("Input: ")
    font = random.choice(list)
    figlet.setFont(font=font)
    print(figlet.renderText(x))

elif len(sys.argv) == 3:
    if sys.argv[1] in  ["-f","--font"]:
        if sys.argv[2] in list:
            x = input("Input: ")
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(x))

        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)

else:
    print("Invalid usage")
    sys.exit(1)

