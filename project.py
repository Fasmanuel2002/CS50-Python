import sys
import webbrowser


def main():
    stocks = {
        "Disney": 83.48,
        "Amazon": 144.85,
        "Tesla": 271.30,
        "Microsoft": 336.06,
        "Meta": 305.06,
        "Apple": 174.21,
        "AT&T": 14.62,
        "Nike": 96.13,
        "Sony": 84.43,
        "Dell": 70.45,
        "Google": 137.50,
        "Baba": 87.64,
        "Starbucks": 96.93,
        "NVDA": 454.85,
        "Paypal": 63.44,
    }

    while True:
        print("A:Buy stocks")
        print("B:Compare stocks")
        print("C:See diagrams of the stock")
        print("D:See news of the stock")
        print("X:Exit\n")
        x = input("What do you want to do? ").capitalize()
        match x:
            case "A":
                buought = buystocks(stocks)
                print(f"${buought:.2f}\n")
            case "B":
                compare = comparestocks(stocks)
                print(f"{compare}\n")

            case "C":
                stocksdiagrams()
            case "D":
                stocksnews()
            case "X":
                break
            case _:
                sys.exit("Bad Letter")


def buystocks(stocks):
    total = 0
    while True:
        stock = input("Stock? ").title()
        number = int(input("How many? "))
        if stock in stocks:
            key = stocks.get(stock)
            print(f"${key * number}")
            total += stocks[stock] * number
        else:
            print("We don't have that stock price SORRY!!!")
            pass
        print("Do you want to buy another stock?")
        choice = input("Yes/No: ").title()
        assert choice in ["Yes", "No"]
        if choice == "Yes":
            continue

        elif choice == "No":
            break
        else:
            print("Only yes or no")
            pass
    return total


def comparestocks(stocks):
    stock1, stock2 = input("What two stocks do you want to compare: ").split("/")

    if stock1 in stocks and stock2 in stocks:
        key = stocks.get(stock1)
        key2 = stocks.get(stock2)
        print(f"${key} and {key2}")
        division = stocks[stock1] / stocks[stock2]
    return f"The value of {stock1} ${stocks[stock1]} is like this compared to {stock2} ${stocks[stock2]} is {division:.2f}"


def stocksdiagrams():
    print("Remember the stock market name is different that the buissness name")
    photo = input("Of this year, what diagram do you want to see? ").upper()
    website = webbrowser.open(
        f"https://finance.yahoo.com/chart/{photo}?ltr=1#https://r.search.yahoo.com/_ylt=AwrLNMoGpQRlyGMKb2ZU04lQ;_ylu=Y29sbwNpcjIEcG9zAzEEdnRpZAMEc2VjA3Nj/RV=2/RE=1694832006/RO=10/RU=https%3a%2f%2fes.finance.yahoo.com%2fquote%2fMSFT%3fp%3dMSFT/RK=2/RS=UlE84FyF6m1OTFxNIcvXQXsi9V0-"
    )


def stocksnews():
    news = input("Of what buissness you want to see news? ").upper()
    website = webbrowser.open(f"https://finance.yahoo.com/quote/{news}/")


if __name__ == "__main__":
    main()

