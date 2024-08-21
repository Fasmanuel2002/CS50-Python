import sys
from PIL import Image
from PIL import ImageOps
import os

if len(sys.argv) == 3:
        
        try:
                user = Image.open(sys.argv[1])
        except FileNotFoundError:
                sys.exit("Input does not exist")
        shirt = Image.open("shirt.png")
        size = shirt.size
        user = ImageOps.fit(user, size)
        user.paste(shirt,shirt)
        
        user.save(sys.argv[2])
        
        
for arg in sys.argv[1:]:
    if arg.endswith(".jpg") or arg.endswith(".png"):
        continue
            
    else:
        sys.exit("Invalid ouetput")      
if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
        
            
        