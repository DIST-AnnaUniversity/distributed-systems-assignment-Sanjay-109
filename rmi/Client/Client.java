import java.rmi.Naming;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
            String serverHostname = "10.11.151.160";
            
            String rmiUrl = "rmi://" + serverHostname + "/CalculatorService";

            Calculator calculator = (Calculator) Naming.lookup(rmiUrl);

            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter first number: ");
            int a = scanner.nextInt();
            System.out.print("Enter second number: ");
            int b = scanner.nextInt();

            System.out.println("Result of addition: " + calculator.add(a, b));
            System.out.println("Result of subtraction: " + calculator.subtract(a, b));
            System.out.println("Result of multiplication: " + calculator.multiply(a, b));
            try {
                System.out.println("Result of division: " + calculator.divide(a, b));
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
            }

            // Close scanner
            scanner.close();
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
