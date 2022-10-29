import java.util.Random;

public class Problem3 {
    public static <string> void main(String[] args) {

        int x1 = (int)(Math.random() * ((90 - 65 + 1)) + 65);
        int x2 = (int)(Math.random() * ((90 - 65 + 1)) + 65);
        int x3 = (int)(Math.random() * ((90 - 65 + 1)) + 65);

        int last4 = (int)(Math.random() * ((9999 - 1000) + 1));

        char c1 = (char) x1;
        char c2 = (char) x2;
        char c3 = (char) x3;

        System.out.println();
        System.out.println(c1 + "" + c2 + "" + c3 + last4);
    }
}
