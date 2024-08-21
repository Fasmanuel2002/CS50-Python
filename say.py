import cowsay
import sys


if len(sys.argv) == 2:
    cowsay.fox("you are just drunk, " + sys.argv[1])