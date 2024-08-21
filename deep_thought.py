x = input("What is the answer to the great question of life, the universe, and Everything?: ")

match x:
    case "42" | "Forty Two" | "forty-two" | "forty two"| "FoRty TwO" | " 42 " :
        print("yes")
        
    case _:
        print("no")