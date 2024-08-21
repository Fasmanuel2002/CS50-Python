from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

#I put down the input because if the if condition doesnt appear
#its going to exit, if not, the programm is going to run


if len(sys.argv) == 1:
    figlet.setFont(font = random.choices())
elif len(sys.argv) == 3 and sys.argv[1] == '-f' and sys.argv[2] == 'slant':
    figlet.setFont(font = 'slant')
elif len(sys.argv) == 3 and sys.argv[1] == '-f' and sys.argv[2] == 'rectangles':
    figlet.setFont(font = 'rectangles')
elif len(sys.argv) == 3 and sys.argv[1] == '-f' and sys.argv[2] == 'alphabet':
    figlet.setFont(font = 'alphabet')
else:
    sys.exit("Invalid usage") 
      
s = input("Input: ")   
print(figlet.renderText(s))