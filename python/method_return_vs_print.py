"""
Exercises to practice the difference between returning values and printing output
"""


def main():
    # Exercise 1: Basic calculation method with return value
    result1 = square(4)
    print(f"The square of 4 is: {result1}")
    
    # Notice how we can use the returned value in another calculation
    doubled_result = result1 * 2
    print(f"The doubled square is: {doubled_result}")
    
    # add another usage of `square`
    
    
    # Exercise 2: Same calculation but with a function that just prints
    print_square(4)
    # We cannot capture the result from print_square for further use
    # This would cause an error:
    # cant_do_this = print_square(4)
    
    # Exercise 3: Chaining calculations with return values
    result3 = add_then_multiply(3, 4, 2)
    print(f"3 + 4, then multiplied by 2 is: {result3}")
    
    # Exercise 4: Return value vs printing in a real scenario
    price = 29.99
    tax_rate = 0.08
    
    # Using a function that returns the tax amount
    tax = calculate_tax(price, tax_rate)
    total_price = price + tax
    print(f"Price: ${price}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total_price}")
    
    # Contrast with just printing the information
    print("\nUsing void function:")
    print_price_with_tax(price, tax_rate)
    
    # Exercise 5: String manipulation
    name = "Python"
    greeting = create_greeting(name)
    print(f"{greeting} Welcome to programming!")
    
    # Exercise 6: Challenge - Maximum number finder
    max_val = find_max(10, 7, 15)
    print(f"The maximum value is: {max_val}")
    
    # Additional example of calculation flow
    num = 5
    squared = square(num)           # returns 25
    cubed = square(num) * num       # returns 125
    fourth_power = square(squared)  # returns 625
    
    print(f"\nPowers of {num}:")
    print(f"Squared: {squared}")
    print(f"Cubed: {cubed}")
    print(f"Fourth power: {fourth_power}")


# Functions that RETURN values

def square(num):
    """
    Returns the square of a number
    """
    return num * num


def print_square(num):
    """
    Prints the square of a number, but doesn't return anything
    why do it this way? why not just
    print(f"The square of {num} is: {square(num)}")
    """
    print(f"The square of {num} is: {num * num}")
    # Notice: no return statement, or "return None" which returns nothing


def add_then_multiply(a, b, multiplier):
    """
    Adds two numbers, then multiplies by a third
    """
    sum_val = a + b
    return sum_val * multiplier


def calculate_tax(price, tax_rate):
    """
    Calculates the tax amount based on price and tax rate
    """
    return price * tax_rate


def create_greeting(name):
    """
    Creates a greeting message for a name
    """
    return f"Hello, {name}!"


def find_max(a, b, c):
    """
    Finds the maximum of three numbers
    """
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val


# Functions that PRINT values (void functions)

def print_price_with_tax(price, tax_rate):
    """
    Prints price information with tax, but doesn't return anything
    VOID is a bad idea here.
    """
    tax = price * tax_rate
    total = price + tax
    print(f"Price: ${price}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total}")
    # The calculated values are inaccessible outside this function


if __name__ == "__main__":
    main()