
x, y ,z = input("Expression: ").split(" ") 
x = int(x)
z = int(z)

if y == "+":    
    sum = x + z
    print(f"{sum:.1f}")

elif y == "-":
    rest = x - z
    print(f"{rest:.1f}")
    
elif y == "*":
    mult = x * z
    print(f"{mult:.1f}")

elif y == "/":
    div = x / z
    print(f"{div:.1f}")
