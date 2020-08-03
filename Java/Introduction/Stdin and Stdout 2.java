import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        double j = scan.nextDouble();
        scan.nextLine();
        String k = scan.nextLine();
        scan.close();
        // Write your code here.

        System.out.println("String: " + k);
        System.out.println("Double: " + j);
        System.out.println("Int: " + i);
    }
}
