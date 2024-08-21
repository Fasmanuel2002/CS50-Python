def main():
    while True:    
        try:
            x,y = input("Fraction:").split("/")
            x = int(x)
            y = int(y)
            divisionr = division(x, y)
            percentage = (divisionr)*100
           
       
            if percentage >= 99:
                print("F")
            elif percentage <= 1:
                print("E")
            elif percentage > 110:
                continue
            
            else: 
                 print(f"{percentage:.0f}%")
            break
        except (ValueError, ZeroDivisionError):
            pass
            
def division(o , k):
    div = o / k 
    return div   
main()