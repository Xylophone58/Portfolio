import java.util.Scanner;

public class Problem6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of rows and columns: ");
        int number = input.nextInt();

        int random = (int) (Math.random() * ((1) + 1));

        //System.out.println(random);

        int i = 0;
        int j = 0;

        String finalString = "";

        for(i = 0; i < number;){
            while(j < number){
                finalString = finalString + (int) (Math.random() * ((1) + 1));
                j++;
            }
            System.out.println(finalString);
            i++;
        }
    }
}
