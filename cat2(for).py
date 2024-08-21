
#j = int(input("Put a number: "))
#for _ in range(j):
 #   print("meow")
#print("meow\n" * 3, end="")



# do when you want to have yes or yes that number
#while True:
#    j = int(input("Put a number: "))
#    if j > 0:
#        break
#for _ in range(j):
 #   print("meow")
 
 
 
 
 
 
 
 
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n =  int(input("Put a number: "))
        if n > 0:
            return n
    
def meow(n):
    for _ in range(n):
        print("meow")
main()