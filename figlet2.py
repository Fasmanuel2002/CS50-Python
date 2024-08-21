from pyfiglet import Figlet

figlet = Figlet()
p = input("in:")

figlet.setFont(font ="slant")


print(figlet.renderText(p))