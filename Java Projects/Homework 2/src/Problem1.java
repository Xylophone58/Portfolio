import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the width: ");
        double width = input.nextDouble();

        System.out.print("Enter the Height: ");
        double height = input.nextDouble();

        System.out.println("Area is " + (width * height));
        System.out.println("Perimeter is " + ((width * 2)+(height * 2)));
    }
}
