# Using Return - One
confusion between System.out.println() and using return statement in a method...

# Return Values vs. Console Output in Java

Learning to distinguish between methods that return values and methods that 
simply output text is a fundamental concept in programming. 
Methods that return values from some set of arguments are easier to test, cleaner to write,
and much more flexible when you need to re-use some logic.
Let's explore this distinction with some explanations and exercises.

## Understanding the Difference

When you're new to programming, it's easy to confuse these two concepts:

### Returning a value 
A method computes something and gives that value back to wherever it was 
called from, allowing further use of that value.

### Printing to console
A method displays text in the console using `System.out.println()`, but doesn't 
make the value available for further computation.

Think of it this way: A method that returns a value is like a calculator that 
shows you the answer on its screen AND lets you use that answer in another calculation. 
A method that just prints is like a calculator that shows the answer but doesn't 
let you use it for anything else.

## Key Differences

```java
// Method that RETURNS a value
public static int add(int a, int b) {
    return a + b;  // Returns the sum to the caller
}

// Method that PRINTS a value
public static void printAdd(int a, int b) {
    System.out.println(a + b);  // Just displays the sum, returns nothing
}
```

With the first method, you can:
```java
int sum = add(5, 3);  // sum now equals 8
int doubled = sum * 2;  // You can use the result in further calculations

//or even...
System.out.println(add(5, 3));
```

With the second method:
```java
printAdd(5, 3);  // Displays "8" to console
// But there's no way to capture that 8 for further use
```

## And in spite of these admonitions

Some of you will try to figure out a way to unit test a method that returns void but prints something to `System.out`.

BEFORE you do _such a thing_, you should read thru [a terrible example.](./TerribleExample.md)
## Practical Exercises

Let's work through some exercises to reinforce this concept:

## Student Exercises

### Exercise 1: Identify the Difference
Review the `square()` and `printSquare()` methods in the code. 
Explain why you can use the result from `square()` in further calculations 
but not the result from `printSquare()`.

### Exercise 2: Fix the Code
Fix this broken code that tries to use a printed value:

```java
public static void main(String[] args) {
    int base = 10;
    int exponent = 2;
    int result = printPower(base, exponent); // Error!
    int doubled = result * 2;
    System.out.println(doubled);
}

public static void printPower(int base, int exponent) {
    int result = (int)Math.pow(base, exponent);
    System.out.println(result);
}
```

### Exercise 3: Convert Methods
Take the `printPriceWithTax()` method and convert it to a method that returns 
the total price instead of printing it.

### Exercise 4: Temperature Converter
Write two versions of a temperature converter:
1. A method that takes Celsius and returns Fahrenheit
2. A method that takes Celsius and prints the Fahrenheit value

Then demonstrate how the first method is more flexible by using its return value in another calculation.

### Exercise 5: Build a Calculator
Create a simple calculator program with separate methods for each 
operation (add, subtract, multiply, divide) that return values. 
Then create a main method that demonstrates chaining these operations together.

## Common Mistakes and Tips

- **Mistake**: Printing a value and thinking it's the same as returning it.
   ```java
   public static int badMethod(int a, int b) {
       System.out.println(a + b);
       // Missing return statement!
   }
   ```
- **Mistake**: Returning a value but forgetting to capture or use it.
```java
square(5); // Calculates 25 but does nothing with it
```
- **Tip**: Methods that perform calculations should typically return their 
results rather than printing them, which makes them more reusable.
- **Tip**: Use meaningful names that indicate what the method returns:
   ```java
   // Good: Name indicates it returns a value
   public static double calculateAreaOfCircle(double radius) {
       return Math.PI * radius * radius;
   }
   
   // Good: Name indicates it prints something
   public static void displayAreaOfCircle(double radius) {
       System.out.println("Area: " + (Math.PI * radius * radius));
   }
   ```

These exercises should help you understand the crucial difference 
between returning values and merely printing them, 
setting the foundation for more advanced programming concepts.