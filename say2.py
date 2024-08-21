import sys #for using system command line

from saying import hello #to import from the "saying.py" the function "Hello"
#its going to ignore the main() because its in a if conditionalp
if len(sys.argv) == 2:
    hello(sys.argv[1])#if the commands user its more than 2, "0" is the name file and 1 the text that the person its going to write 