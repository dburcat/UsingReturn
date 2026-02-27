package rocks.zipcode;
/**
 * Exercises to practice the difference between returning values and printing output
 */
public class MethodReturnVsPrint {

    public static void main(String[] args) {
        // Exercise 1: Basic calculation method with return value
        int result1 = square(4);
        System.out.println("The square of 4 is: " + result1);

        // Notice how we can use the returned value in another calculation
        int doubledResult = result1 * 2;
        System.out.println("The doubled square is: " + doubledResult);

        // add another usage of `square`


        // Exercise 2: Same calculation but with a void method that just prints
        printSquare(4);
        // We cannot capture the result from printSquare for further use
        // This would cause a compiler error:
        // int cantDoThis = printSquare(4);

        // Exercise 3: Chaining calculations with return values
        int result3 = addThenMultiply(3, 4, 2);
        System.out.println("3 + 4, then multiplied by 2 is: " + result3);

        // Exercise 4: Return value vs printing in a real scenario
        double price = 29.99;
        double taxRate = 0.08;

        // Using a method that returns the tax amount
        double tax = calculateTax(price, taxRate);
        double totalPrice = price + tax;
        System.out.println("Price: $" + price);
        System.out.println("Tax: $" + tax);
        System.out.println("Total: $" + totalPrice);

        // Contrast with just printing the information
        System.out.println("\nUsing void method:");
        printPriceWithTax(price, taxRate);

        // Exercise 5: String manipulation
        String name = "Java";
        String greeting = createGreeting(name);
        System.out.println(greeting + " Welcome to programming!");

        // Exercise 6: Challenge - Maximum number finder
        int max = findMax(10, 7, 15);
        System.out.println("The maximum value is: " + max);

        // Additional example of calculation flow
        int num = 5;
        int squared = square(num);           // returns 25
        int cubed = square(num) * num;       // returns 125
        int fourthPower = square(squared);   // returns 625

        System.out.println("\nPowers of " + num + ":");
        System.out.println("Squared: " + squared);
        System.out.println("Cubed: " + cubed);
        System.out.println("Fourth power: " + fourthPower);
    }

    // Methods that RETURN values

    /**
     * Returns the square of a number
     */
    public static int square(int num) {
        return num * num;
    }
    /**
     * Prints the square of a number, but doesn't return anything
     * why do it this way? why not just
     * System.out.println("The square of " + num + " is: " + square(num));
     */
    public static void printSquare(int num) {
        System.out.println("The square of " + num + " is: " + (num * num));
        // Notice: no return statement, or "return;" which returns nothing
    }


    /**
     * Adds two numbers, then multiplies by a third
     */
    public static int addThenMultiply(int a, int b, int multiplier) {
        int sum = a + b;
        return sum * multiplier;
    }

    /**
     * Calculates the tax amount based on price and tax rate
     */
    public static double calculateTax(double price, double taxRate) {
        return price * taxRate;
    }

    /**
     * Creates a greeting message for a name
     */
    public static String createGreeting(String name) {
        return "Hello, " + name + "!";
    }

    /**
     * Finds the maximum of three numbers
     */
    public static int findMax(int a, int b, int c) {
        int max = a;
        if (b > max) {
            max = b;
        }
        if (c > max) {
            max = c;
        }
        return max;
    }

    // Methods that PRINT values (void methods)


    /**
     * Prints price information with tax, but doesn't return anything
     * VOID is a bad idea here.
     */
    public static void printPriceWithTax(double price, double taxRate) {
        double tax = price * taxRate;
        double total = price + tax;
        System.out.println("Price: $" + price);
        System.out.println("Tax: $" + tax);
        System.out.println("Total: $" + total);
        // The calculated values are inaccessible outside this method
    }
}