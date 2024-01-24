import sys
from pyfiglet import Figlet, FigletFont
import random

def main():
    # Check command line arguments
    if len(sys.argv) == 1:
        f = Figlet(font=random.choice(FigletFont.getFonts()))  
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        try:
            f = Figlet(font=sys.argv[2])
        except Exception as e:
            print(f'Error: {e}')
            sys.exit(1)
    else:
        print('Error: Invalid command line arguments')
        sys.exit(1)

    # Prompt user for the text
    text = input("Enter your text: ")
    
    # Output the formatted text
    print(f.renderText(text))

if __name__ == "__main__":
    main()