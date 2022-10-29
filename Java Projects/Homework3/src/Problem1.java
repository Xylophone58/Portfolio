import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Please enter an integer => ");
        double number = input.nextDouble();

        if(number % 2 == 1){
            System.out.println(number + " is odd");
        }
        else{
            System.out.println(number + " is even");
        }
    }
}
