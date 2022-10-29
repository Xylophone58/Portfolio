//Zachary Mitchell
//displays three numbers in increasing order

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);


        //gets user input
        System.out.print("Enter Number 1: ");
        int number1 = input.nextInt();

        System.out.print("Enter Number 2: ");
        int number2 = input.nextInt();

        System.out.print("Enter Number 3: ");
        int number3 = input.nextInt();

        //calls the below method
        displaySortedNumbers(number1, number2, number3);
    }
    public static void displaySortedNumbers(int num1, int num2, int num3){

        //puts numbers into list for easier method of sorting
        List<Integer> list = Arrays.asList(num1,num2,num3);
        Collections.sort(list);

        int i = 0;
        //uses while loop to print numbers (without brackets and commas)
        while(i < list.size()){
            System.out.print(list.get(i) + " ");
            i++;
        }
    }
}
