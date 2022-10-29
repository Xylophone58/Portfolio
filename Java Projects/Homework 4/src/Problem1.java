import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Please enter a number between 0 and 2: ");
        double number = input.nextDouble();

        int random = 0 + (int)(Math.random() * ((2 - 0) + 1));

        System.out.println(random);
        
        if(number < 0 || number > 2){
            System.out.println("Invalid Range. Please try again");
        } else if (number == random) {
            System.out.println("Its a Tie!");
        } else if ((number == 0 && random == 1) || (number == 1 && random == 2) || (number == 2 && random == 0)) {
            System.out.println("You Lost!");
        } else if ((number == 0 && random == 2) || (number == 1 && random == 0) || (number == 2 && random == 1)) {
            System.out.println("You Won!");
        }
    }
}
