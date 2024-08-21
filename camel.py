def main():
    f = input("camelCase: ")

    for c in f:
        if find(f):        
            print(f"snake_case: {c}")
            
            
def find(fi):
    if fi:
        return True
    else:
        print("you are bad")

main()
