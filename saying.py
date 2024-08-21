def main():
    
    hello("world")
    goodbye("world")




def hello(name):
    print(f"Hello, {name}")
    
    
def goodbye(name):
    print(f"Goodbye, {name}")


if __name__ == "__main__":#this is going to make that main doesnt apply everything, just the function we want to use
    main()#its going to run only when I run the progam