import java.util.Scanner;

public class Problem3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Please enter a string: ");
        String str = input.nextLine();

        String strUpper = str.toUpperCase();

        //System.out.println(strUpper);

        int i = 0;
        int vowels = 0;
        int consonants = 0;

        while(i < strUpper.length()){

            char character = strUpper.charAt(i);

            if(character == 'A' || character == 'E' || character == 'I' || character == 'O' || character == 'U'){
                vowels+=1;

            }else
                consonants+=1;
            i+=1;
        }
        System.out.println("The number of Vowels is: " + vowels);
        System.out.println("The number of Consonants is: " + consonants);
    }
}

