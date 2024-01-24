def get_greeting():
    greeting = input("Type your greeting: ")
    greeting = greeting.strip().lower()
    if "hello" in greeting:
       print("$0")
    elif greeting[0] == "h" and greeting[1] != "e":
       print("$20")
    else: print("$100")

    