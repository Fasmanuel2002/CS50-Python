x = input("Greeting: ")

x = x.capitalize()


match x:
    case "How you doing?" | "Hey":
        print("$20")
    case "What's happening?":
        print("$100")
    case "Hello" | "Hello, Newman":
        print("$0")