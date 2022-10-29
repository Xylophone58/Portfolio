import java.util.Scanner;

public class Problem2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int i = 1;
        double finalNumber = 0;
        double amount = 0;
        while (i != 0) {
            System.out.print("Please enter a values and terminate with 0: ");
            int newInput = input.nextInt();
            i = newInput;
            amount++;

            finalNumber += newInput;

        }

        double average = finalNumber / amount;

        System.out.println("The sum is: " + finalNumber);
        System.out.println("The Average is: " + average);

    }
}
