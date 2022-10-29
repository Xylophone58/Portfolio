//Zachary Mitchell
//counts how many times a certain character appears in a string

import java.util.Scanner;

public class Problem3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        //gets both string and character
        System.out.print("Enter a String: ");
        String string = input.next();

        System.out.print("Enter a Character: ");
        String characterString = input.next();

        //sets the string to a character
        char character = characterString.charAt(0);

        //calls the below method
        System.out.println(count(string, character));
    }
    public static int count(String str, char aCharacter){

        //number for how many times a number is repeated
        int lettersRepeated = 0;

        //loops through length of the string
        for(int i = 0; i < str.length(); i++){
            char testChar = str.charAt(i);
            if(testChar == aCharacter){
                lettersRepeated++;
            }
        }
        //returns the exact amount that the character was repeated
        return lettersRepeated;
    }
}
