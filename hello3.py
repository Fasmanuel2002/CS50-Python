def main():
    name = input("What's your name?: ")
    print(hello(name))#here you are just printing the function
    
    
def hello(to="world"):
    return f"hello, {to}"#here you are returning the value of hello world
    
if __name__ == "__main__":
    main()