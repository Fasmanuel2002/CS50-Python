def main():  
        try:  
                taco = input("Item: ").title()
    
        
                d = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
                }

                        
                if taco in d:
                        key = d.get(taco)
                        print(f"${key}")
                        sum(key, key)
        except EOFError:
                pass               
                        
        
                        
        
                        


def sum(a,b):
        sum =  a + b
        return sum
main()
                        