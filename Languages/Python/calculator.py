print("commands: add / sub / mul / div / mod / pow / fdiv")
print("mod - remainder after dividing")
print("pow - num1 to the power of num2")
print("fdiv - division result is a whole number")

command = str(input("Which command?: "))

first = int(input("first number: "))

second = int(input("second number: "))

def whichoperator(command, num1, num2):
    match command:
        case "add":
            return num1 + num2
        case "sub":
            return num1 - num2
        case "mul":
            return num1 * num2
        case "div":
            return num1 / num2
        case "mod":
            return num1 % num2
        case "pow":
            return num1 ** num2
        case "fdiv":
            return num1 // num2
        case _:
            return "invalid command"

print(whichoperator(command, first, second))
