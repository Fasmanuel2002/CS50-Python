def main():
    col = int(input("How many columns: "))
    print_column(col)
    



def print_column(height):
    for _ in range(height):
        print("#")
main()