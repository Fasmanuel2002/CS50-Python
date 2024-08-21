def main():

    x = get_int()
    print(f"x is {x}")

def get_int():
    #its going to try this
    while True:
        try:
            x = int(input("X: ")) 
        #if it doesnt work; its going to be here 
        except ValueError:
            print("x is not a string")
        #if it is good; its going to run this
        else:   
         
        #handback a value
            return x #stronger than break
    
main()