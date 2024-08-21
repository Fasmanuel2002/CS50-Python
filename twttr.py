import sys

def main():
    word = input("Input: ")
    print(shorten(word))



def shorten(shorten):
    newtest = ""
    vowels = ["a", "e", "i", "o", "u"]
   
    try:
        for i in range(len(shorten)):
            if shorten[i].lower() not in vowels:
                newtest += shorten[i]   
            
    except TypeError:
            SystemExit
    return newtest
   
          


if __name__ == "__main__":
    main()