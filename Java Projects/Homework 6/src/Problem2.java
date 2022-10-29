import java.util.Scanner;

public class Problem2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a SSN: ");
        String txt = input.next();

        String[] SSN = txt.split("-", 3);

        String part1 = SSN[0];
        String part2 = SSN[1];
        String part3 = SSN[2];

        if(part1.length() == 3 && part2.length() == 2 && part3.length() == 4){
            System.out.println(txt + " is a valid Social Security Number");
        }else{
            System.out.println(txt + " is an invalid Social Security Number");
        }

    }
}
