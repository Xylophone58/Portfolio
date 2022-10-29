//Write a program that prompts the user to
//enter a String and displays the first character
//and
//displays whether the string has 3 or more characters long.

import java.util.Scanner;

public class CodeSprint4{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.print("Please enter a string: ");
        String str = input.nextLine();

        //Display whether str has three or more characters.  hint length()
        if(str.length() >= 3){
            System.out.println("This String has 3 or more characters");
        }


        //Display the first character of str, hint charAt()

        System.out.println("the first character in the string is " + str.charAt(0));

    }
}


