score = int(input("Score: "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 60:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")