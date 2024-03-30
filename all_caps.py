print("Welcome to Adam's py tools")
tool_select = input("Which tool would you like to use? type: caps for capitalizer, add for adderatorinator")

if (tool_select == "caps"):
    print("Welcome to the capitalizer (my first python cli tool)")
    word = input("What would you like me to capitalize?")
    print(f"Here is your capitalized string: {word.upper()}")
elif (tool_select == "add"):
    num1 = int(input("Welcome to the adderatorinator. Type your first number:"))
    num2 = int(input("Type your second number:"))
    print(f"{num1} + {num2} = {num1 + num2}")
