import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Please enter a number: ");
        int number = input.nextInt();

        System.out.println("Multiplication table for " + number);
        System.out.println("Multiplier     Result");
        System.out.println("---------------------");

        int i = 1;

        while(i <= 10){
            System.out.println("    " + i + "           " + (i * number));
            i++;
        }
    }
}
