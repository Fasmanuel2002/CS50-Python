import sys
if len(sys.argv) == 2:
    try:
        
        with open(sys.argv[1]) as file:
            nlines = 0
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip() !='':
                    nlines += 1
        print(nlines)
    except FileExistsError:
        sys.exit("File does not exist")
    

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments") 

if len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")
    
for arg in sys.argv[1:]:
    if arg.endswith(".py"):
        continue
        
    else:
        sys.exit("Not a Python file")    


