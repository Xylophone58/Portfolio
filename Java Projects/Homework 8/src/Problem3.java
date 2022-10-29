import java.util.Scanner;

public class Problem3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Starting Number: ");
        int realstart = input.nextInt();

        System.out.print("Enter Ending Number: ");
        int end = input.nextInt();

        int start = realstart;

        int remainder = start % 4;

        String numbers = "";

        while(remainder != 0){
            start++;
            remainder = start % 4;
        }

        while(start <= end){
            numbers = numbers + start + " ";
            start = start + 4;
        }

        System.out.println("Multiples of 4 between " + realstart + " and " + end + " include: " + numbers);
    }
}
