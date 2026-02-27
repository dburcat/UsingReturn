
def main():
    num1 = 42
    num2 = 96

    print(f"The sum of {num1} and {num2} is: {addit(num1, num2)}")
    print(f"The difference of {addit(num1, num2)} and {num2} is: {subtract(addit(num1, num2), num2)}")
    print(f"The product of {addit(num1, num2)} and {num1} is: {multiply(addit(num1, num2), num1)}")
    print(f"The quotient of {multiply(addit(num1, num2), num1)} and {subtract(addit(num1, num2), num2)} is: {divide(multiply(addit(num1, num2), num1), subtract(addit(num1, num2), num2))}")

def addit(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

if __name__ == "__main__":
    main()