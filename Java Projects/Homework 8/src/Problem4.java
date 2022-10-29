public class Problem4 {
    public static void main(String[] args) {
        String Numbers = "";
        int i = 0;

        for(i = 100; i >= 55;){
            Numbers = Numbers + i + " ";
            i = i - 5;
        }
        System.out.println(Numbers);
    }
}
