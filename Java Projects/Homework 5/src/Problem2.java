import java.util.Scanner;

public class Problem2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a Letter: ");
        String letter = input.next();

        letter = letter.toUpperCase();

        if(!letter.matches("[A-Z]+")) {
            System.out.println("Invalid Statement");
        }else{
            switch (letter) {
                case "A", "B", "C" -> System.out.println("1");
                case "D", "E", "F" -> System.out.println("2");
                case "G", "H", "I" -> System.out.println("3");
                case "J", "K", "L" -> System.out.println("4");
                case "M", "N", "O" -> System.out.println("5");
                case "P", "Q", "R", "S" -> System.out.println("6");
                case "T", "U", "V" -> System.out.println("7");
                case "W", "X", "Y", "Z" -> System.out.println("9");
            }

        }

    }
}
