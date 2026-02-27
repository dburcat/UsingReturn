# Ugh

## This is such a bad idea

### Don't EVER do this

### No really.

If you absolutely must create a unit test for the original `void` method that 
prints to standard output, you'll need to capture and verify the console output. 
Here's how to do it using JUnit:

```java
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import static org.junit.Assert.*;

public class PricePrinterTest {
    // Set up streams to capture stdout
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;
    
    @Before
    public void setUpStreams() {
        // Redirect System.out to our ByteArrayOutputStream
        System.setOut(new PrintStream(outContent));
    }
    
    @After
    public void restoreStreams() {
        // Restore System.out to its original state
        System.setOut(originalOut);
    }
    
    @Test
    public void testPrintPriceWithTax() {
        // Given
        double price = 29.99;
        double taxRate = 0.08;
        
        // Expected output (careful with line endings and formatting)
        String expectedOutput = "Price: $29.99" + System.lineSeparator() +
                               "Tax: $2.3992" + System.lineSeparator() +
                               "Total: $32.3892" + System.lineSeparator();
        
        // When
        printPriceWithTax(price, taxRate);
        
        // Then
        assertEquals(expectedOutput, outContent.toString());
    }
    
    @Test
    public void testPrintPriceWithZeroTax() {
        // Given
        double price = 50.0;
        double taxRate = 0.0;
        
        // Reset output from previous tests
        outContent.reset();
        
        // Expected output
        String expectedOutput = "Price: $50.0" + System.lineSeparator() +
                               "Tax: $0.0" + System.lineSeparator() +
                               "Total: $50.0" + System.lineSeparator();
        
        // When
        printPriceWithTax(price, taxRate);
        
        // Then
        assertEquals(expectedOutput, outContent.toString());
    }
    
    /**
     * This is the original method being tested
     */
    public static void printPriceWithTax(double price, double taxRate) {
        double tax = price * taxRate;
        double total = price + tax;
        System.out.println("Price: $" + price);
        System.out.println("Tax: $" + tax);
        System.out.println("Total: $" + total);
    }
}
```

Key points about this approach:

1. It uses `ByteArrayOutputStream` to capture what's printed to `System.out`
2. It sets up stream redirection before each test and restores the original stream afterward
3. It includes exact expected output with system-specific line separators
4. It tests against the entire text output, making it brittle to changes in formatting

This approach has several drawbacks:

- Tests are fragile and sensitive to formatting changes
- Even minor changes to output format break the tests
- Tests depend on system-specific line endings
- Tests don't clearly communicate intent (they test string output, not business logic)
- Double precision formatting might be inconsistent across platforms

That's why returning values and testing the actual calculation logic is strongly 
preferred over testing console output. 

But if you're just too **bull-headed** to see reason,
constraints require testing the void method directly, this approach works. Mostly. Kinda.