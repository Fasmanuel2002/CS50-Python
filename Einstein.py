def main():
    x = int(input("m: "))
    
    y = 300000000 
    x = x * square(y)
    
    print(f"E:{x}")








def square(n):
    return pow(n , 2)
    
main()