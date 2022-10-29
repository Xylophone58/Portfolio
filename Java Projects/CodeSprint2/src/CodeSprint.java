import java.util.Scanner;

public class CodeSprint {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Please enter a base number: ");
        double number = input.nextDouble();

        System.out.print("Please enter the multiple:");
        double multiple = input.nextDouble();

        if(number % multiple == 0){
            System.out.println(number + " is a multiple of " + multiple);
        }
        else{
            System.out.println(number + " is not a multiple of " + multiple);
        }
    }
}
