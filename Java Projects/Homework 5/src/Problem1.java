import java.sql.SQLOutput;
import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Please enter a number between 0 and 2: ");
        int number = (int) input.nextDouble();

        int random = 0 + (int)(Math.random() * ((2 - 0) + 1));

        System.out.println(random);

        if(number < 0 || number > 2){
            System.out.println("Invalid Range. Please try again");
        } else{
            switch (number){
                case 0: if(random == 1){
                    System.out.println("You Lost!");
                }else if(random == 2){
                    System.out.println("You Won!");
                }else System.out.println("Its a tie!");
                break;

                case 1: if(random == 2){
                    System.out.println("You Lost!");
                }else if(random == 0){
                    System.out.println("You Won!");
                }else System.out.println("Its a tie!");
                break;

                case 2: if(random == 0){
                    System.out.println("You Lost!");
                }else if(random == 1){
                    System.out.println("You Won!");
                }else System.out.println("Its a tie!");
                break;
            }
        }
    }
}
