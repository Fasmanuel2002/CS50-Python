def main():

    number = int(input("Whats the number: "))
    if is_even(number):
          print("It's even") 
    else:
        print("its odd")

    

def is_even(n):
   return True if n % 2 == 0 else False
main()

