# Using Return - Python Version

Confusion between `print()` and using return statement in a function...

# Return Values vs. Console Output in Python

Learning to distinguish between functions that return values and functions that 
simply output text is a fundamental concept in programming. 
Functions that return values from some set of arguments are easier to test, cleaner to write,
and much more flexible when you need to re-use some logic.
Let's explore this distinction with some explanations and exercises.

## Understanding the Difference

When you're new to programming, it's easy to confuse these two concepts:

### Returning a value 
A function computes something and gives that value back to wherever it was 
called from, allowing further use of that value.

### Printing to console
A function displays text in the console using `print()`, but doesn't 
make the value available for further computation.

Think of it this way: A function that returns a value is like a calculator that 
shows you the answer on its screen AND lets you use that answer in another calculation. 
A function that just prints is like a calculator that shows the answer but doesn't 
let you use it for anything else.

## Key Differences

```python
# Function that RETURNS a value
def add(a, b):
    return a + b  # Returns the sum to the caller

# Function that PRINTS a value
def print_add(a, b):
    print(a + b)  # Just displays the sum, returns None
```

With the first function, you can:
```python
sum_result = add(5, 3)  # sum_result now equals 8
doubled = sum_result * 2  # You can use the result in further calculations

# or even...
print(add(5, 3))
```

With the second function:
```python
print_add(5, 3)  # Displays "8" to console
# But there's no way to capture that 8 for further use
```

## Running the Code

### Running the main program:
```bash
python method_return_vs_print.py
```

### Running the tests:
```bash
python test_method_return_vs_print.py
```

## Practical Exercises

Let's work through some exercises to reinforce this concept:

## Student Exercises

### Exercise 1: Identify the Difference
Review the `square()` and `print_square()` functions in the code. 
Explain why you can use the result from `square()` in further calculations 
but not the result from `print_square()`.

### Exercise 2: Fix the Code
Fix this broken code that tries to use a printed value:

```python
def main():
    base = 10
    exponent = 2
    result = print_power(base, exponent)  # Error!
    doubled = result * 2
    print(doubled)

def print_power(base, exponent):
    result = base ** exponent
    print(result)
```

### Exercise 3: Convert Functions
Take the `print_price_with_tax()` function and convert it to a function that returns 
the total price instead of printing it.

### Exercise 4: Temperature Converter
Write two versions of a temperature converter:
1. A function that takes Celsius and returns Fahrenheit
2. A function that takes Celsius and prints the Fahrenheit value

Then demonstrate how the first function is more flexible by using its return value in another calculation.

### Exercise 5: Build a Calculator
Create a simple calculator program with separate functions for each 
operation (add, subtract, multiply, divide) that return values. 
Then create a main function that demonstrates chaining these operations together.

## Common Mistakes and Tips

- **Mistake**: Printing a value and thinking it's the same as returning it.
   ```python
   def bad_function(a, b):
       print(a + b)
       # Missing return statement!
   ```
- **Mistake**: Returning a value but forgetting to capture or use it.
```python
square(5)  # Calculates 25 but does nothing with it
```
- **Tip**: Functions that perform calculations should typically return their 
results rather than printing them, which makes them more reusable.
- **Tip**: Use meaningful names that indicate what the function returns:
   ```python
   # Good: Name indicates it returns a value
   def calculate_area_of_circle(radius):
       return 3.14159 * radius * radius
   
   # Good: Name indicates it prints something
   def display_area_of_circle(radius):
       print(f"Area: {3.14159 * radius * radius}")
   ```

These exercises should help you understand the crucial difference 
between returning values and merely printing them, 
setting the foundation for more advanced programming concepts.