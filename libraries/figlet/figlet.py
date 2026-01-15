
import pyfiglet
import random
import sys


def main():
    figlet=pyfiglet.Figlet()
    fonts=figlet.getFonts()

    if len(sys.argv)==1:
        font=random.choice(fonts)
    elif len(sys.argv)==3:
        if sys.argv[1] in ["-f","--font"] and sys.argv[2] in fonts:
            font=sys.argv[2] # We've the selected font here from fonts
        else:
            sys.exit("Invalid usage")

    else: 
        sys.exit("invalid usage")

    data=input("Input: ")

    # this line connects to the figlet engine
    figlet.setFont(font=font) 

    print(f"Output: {figlet.renderText(data)}")

main()



