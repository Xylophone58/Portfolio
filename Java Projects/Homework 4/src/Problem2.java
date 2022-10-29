import java.util.Scanner;

public class Problem2 {
    public static void main(String[] args) {
        int lottery_1 = (int)(Math.random() * 10);
        int lottery_2 = (int)(Math.random() * 10);

        // Prompt the user to enter a guess
        Scanner input = new Scanner(System.in);
        System.out.print("Enter number 1: ");
        double guess1 = input.nextInt();

        System.out.print("Enter number 2: ");
        double guess2 = input.nextInt();

        if(guess1 == lottery_1 && guess2 == lottery_2 || guess2 == lottery_1 && guess1 == lottery_2){

            System.out.print("You got both numbers correct!");

        } else if (guess1 == lottery_1 || guess1 == lottery_2 || guess2 == lottery_1 || guess2 == lottery_2) {
            System.out.print("you got a number correct!");
        }else{
            System.out.print("you got it wrong!");
        }

        System.out.println(lottery_1);
        System.out.println(lottery_2);
    }
}
