def main():
    try:
            x = int(input("What's x?: "))
            print("x squared is:", square(x))
    except ValueError:
        print("Not a string")       
    
def square(n):
    return n * n
if __name__ == "__main__":#we use this because its when you import the function to another program
    main()
    