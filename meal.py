def main():
        
    hour, min = input("What time is it: ").split(":")
    hour = float(hour)
    min = float(min)
    if (hour >= "8:00") or hour and min <= "7:00":
        print("breakfast time:") 
main()