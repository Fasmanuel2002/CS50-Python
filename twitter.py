twi = input("Input: ")


for c in twi:
    c = c.removeprefix("a").removeprefix("e").removeprefix("i")    
    c = c.removeprefix("o").removeprefix("u").removeprefix("O")
    print(c, end="")