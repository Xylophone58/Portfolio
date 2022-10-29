import java.util.Scanner;

public class Problem3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("enter a 4 digit number: ");
        int mainNumber = input.nextInt();

        int thousands = (mainNumber / 1000) % 10;
        int hundreds = (mainNumber / 100) % 10;
        int tens = (mainNumber / 10) % 10;
        int ones = (mainNumber / 1) % 10;

        if(thousands == ones && hundreds == tens){
            System.out.println("This is a palindrome");
        }else{
            System.out.println("This is not a palindrome");
        }
    }
}
