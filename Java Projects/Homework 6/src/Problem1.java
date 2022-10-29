import java.util.Scanner;
import java.lang.String;

public class Problem1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Please enter an amount: ");
        String txt = input.next();

        String[] money = txt.split("\\.", 2);

        String dollarsX = money[0];
        String cents = money[1];

        String dollars = dollarsX.replaceAll("[$]", "");

        System.out.println("There are " + dollars + " dollars and " + cents + " cents");
    }
}
