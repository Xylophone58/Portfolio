public class Problem3 {
    public static void main(String[] args) {
        String team = "Chiefs";
        int week = 4;
        int wins = 1;
        int losses = 2;
        int tie = 0;
        double pct = .3333333;

        System.out.printf(team + " Week " + week + " Statistics\n");
        System.out.printf(" Wins  Loss  Tie      PCT\n");
        System.out.printf("    " + wins + "     " + losses + "    " + tie + "    " + String.format("%.3g%n", pct));
    }
}
