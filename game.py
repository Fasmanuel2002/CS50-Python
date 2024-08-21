import random

# the are asking for a game that is to guess, if you guess the number it fini


def main():
    l = random.randrange(100)
    n = get_int()
    l = get_l()

    if n == l:
        print("Just Right!")

    elif n > l:
        print("Too small!")
    else:
        print("Too large!")


def get_int():
    while True:
        try:
            n = int(input("Level: "))
            if n < 0:
                raise ValueError    

        except (ValueError, IndexError):
            pass
        else:
            return n


def get_l():
    while True:
        try:
            l = int(input("Guess: "))
            if l < 0:
                raise ValueError    

        except ValueError:
            pass
        else:
            return l


main()
