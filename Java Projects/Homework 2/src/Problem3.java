import java.util.Scanner;

public class Problem3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the subtotal of the bill: ");
        double sub = input.nextDouble();

        System.out.print("Enter gratuity rate: ");
        double GR = input.nextDouble();

        double amount = (sub * GR / 100);

        double total = amount + sub;

        System.out.println("The amount of gratuity is $" + amount);

        System.out.println("The total final bill is $" + total);
    }
}
