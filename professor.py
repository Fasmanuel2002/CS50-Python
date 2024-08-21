# EEE when you are bad
import random
def main():
    
   
    n = get_level()
    lvl = generate_integer(n)
    
    print(f"Score: {lvl}")
    
    
    
    

def get_level():
   while True:
        try:
            n = int(input("Level: "))
            if n != 1 and n != 2 and n != 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return n
    


def generate_integer(level):
            
            contador = 0
            if level == 1:
                for _ in range(10):
                    x = random.randrange(10)
                    y = random.randrange(10)
                    for _ in range(3):
                        level = int(input(f"{x} + {y} = "))
                        sum = x + y
                        if sum == level:
                            contador += 1
                            break
                        else:
                            print("EEE")
                    print(sum)
            if level == 2:
                for _ in range(10):
                    x = random.randrange(10, 99)
                    y = random.randrange(10, 99)
                    level = int(input(f"{x} + {y} = "))
                    sum = x + y
                    if sum == level:
                        contador += 1
                
                    else:
                        print("EEE")
            if level == 3:
                for _ in range(10):
                    x = random.randrange(100, 999)
                    y = random.randrange(100, 999)
                    level = int(input(f"{x} + {y} = "))
                    sum = x + y
                    if sum == level:
                        contador += 1
                
                    else:
                        print("EEE")      
                   
            return contador
    
    


if __name__ == "__main__":
    main()