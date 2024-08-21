def main():
    coke = int(50)
    print(f"Amount due: {coke}")

    while True:
        coin = int(input("Insert coin: "))
        coke = resta = int(rest(coke, coin))
        if resta != 0 and coin <= 50:
            print(f"Amount Due: {coke}")
            continue
        elif resta == 0:
            print(f"Change Owed: {resta}")
            break


def rest(c, co):
    restation = c - co
    return restation


main()
