import java.util.Scanner;

public class Problem5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Please enter number 1: ");
        int number1 = input.nextInt();

        System.out.print("Please enter number 2: ");
        int number2 = input.nextInt();

        System.out.print("Please enter number 3: ");
        int number3 = input.nextInt();

        System.out.print("Please enter number 4: ");
        int number4 = input.nextInt();

        System.out.print("Please enter number 5: ");
        int number5 = input.nextInt();

        System.out.print("Please enter number 6: ");
        int number6 = input.nextInt();

        System.out.print("Please enter number 7: ");
        int number7 = input.nextInt();

        System.out.print("Please enter number 8: ");
        int number8 = input.nextInt();

        System.out.print("Please enter number 9: ");
        int number9 = input.nextInt();

        System.out.print("Please enter number 10: ");
        int number10 = input.nextInt();

        int test1 = Math.max(number1, number2);
        int test2 = Math.max(number3, number4);
        int test3 = Math.max(number5, number6);
        int test4 = Math.max(number7, number8);
        int test5 = Math.max(number9, number10);

        int test10 = Math.max(test1, test2);
        int test11 = Math.max(test3, test4);

        int test20 = Math.max(test10, test11);

        int finalTest = Math.max(test20, test5);

        System.out.println("the Largest value is: " + finalTest);
    }
}
