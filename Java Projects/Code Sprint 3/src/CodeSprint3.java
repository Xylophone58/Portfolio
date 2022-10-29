//This program reads an integer that represents a test grade.
//The program displays the appropriate
//letter grade based on the following rules.


// 8 <= grade <= 10 is an A
// 5 <= grade <=7 is a B
// grade < 5 is a C.

import java.util.Scanner;

public class CodeSprint3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter grade
        System.out.print("Enter score (1-10): ");
        int grade = input.nextInt();

        if(grade >=8 && grade <= 10){
            System.out.println("Grade: A");
        } else if (grade >=5 && grade <= 7) {
            System.out.println("Grade: B");
        }else System.out.println("Grade: C");
    }
}