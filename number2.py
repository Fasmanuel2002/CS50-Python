def main():

    x = get_int("What's x? ")
    print(f"x is {x}")

# like a i want ""
def get_int(prompt):
    #its going to try this
    while True:
        try:
            return int(input(prompt)) #here put a prompt
        #if it doesnt work; its going to be here 
        except ValueError:
            pass #do again
        #if it is good; its going to run this
        
    
main()



#                 
  