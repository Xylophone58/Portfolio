import java.util.Scanner;

public class Problem2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Kilograms     Pounds");
        System.out.println("---------------------");

        double i = 0;

        for (i = 1; i < 20; i = i + 2) {
            System.out.printf("%-14.0f%1.1f \n", i, (i * 2.2));
        }
    }
}
