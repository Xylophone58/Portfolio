import java.util.Scanner;
import java.lang.Math;

public class Problem2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the radius: ");
        double radius = input.nextDouble();

        double pi = 3.14159;

        System.out.println("Area: " + ((4 * pi) * Math.pow(radius, 2)));

        System.out.println("Volume: " + ((4.0/3) * pi * Math.pow(radius, 3)));
    }
}
