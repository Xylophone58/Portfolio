//Zachary Mitchell
//converts text to a keypad number

import java.util.Scanner;

public class Problem2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        //gets user input for string
        System.out.print("Enter a String: ");
        String origString = input.next();

        origString = origString.toUpperCase();

        String finalNumber = "";


        //main loop that checks if there is any letters. if there are, then it is sent to the below method.
        for(int i = 0; i < origString.length(); i++) {

            char letter = origString.charAt(i);

            if (Character.isLetter(letter)) {
                finalNumber += letterToNumber(letter);
            }else {
                finalNumber += letter;
            }

        }
        System.out.println(finalNumber);
    }


    private static int letterToNumber(char letter) {
        int number = 0;

        switch (letter) {
            case 'A', 'B', 'C' -> number = 2;
            case 'D', 'E', 'F' -> number = 3;
            case 'G', 'H', 'I' -> number = 4;
            case 'J', 'K', 'L' -> number = 5;
            case 'M', 'N', 'O' -> number = 6;
            case 'P', 'Q', 'R', 'S' -> number = 7;
            case 'T', 'U', 'V' -> number = 8;
            case 'W', 'X', 'Y', 'Z' -> number = 9;
        }

        return number;
    }
}
