import sys

#check errors
if len(sys.argv) < 2:
    sys.exit("Too few Arguments")
# this is thing is a slice, from to make an start from the array
for arg in sys.argv[1:]: #having a negative number its the effect of elimating the last numbers
    # to say something, is like the input value and you do with sys.argv
    print("hello, my is" , arg)# this "1" is storing the string
    #0 in the list its the name of the progam == name.py
