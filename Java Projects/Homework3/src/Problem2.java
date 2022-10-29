import java.util.Scanner;

public class Problem2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the length of line 1: ");
        double line1 = input.nextDouble();

        System.out.print("Enter the length of line 2: ");
        double line2 = input.nextDouble();

        System.out.print("Enter the length of line 3: ");
        double line3 = input.nextDouble();

        if(line1 + line2 <= line3){
            System.out.println("The Sides " + line1 + " " + line2 + " " + line3 + " make an illegal triangle");
        }
        else{
            System.out.println("The perimeter is " + (line1 + line2 + line3));
        }
    }
}
