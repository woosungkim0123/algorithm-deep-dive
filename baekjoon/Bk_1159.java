import java.util.Scanner;

public class Bk_1159 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int arr[] = new int[26];
        for (int i = 0; i < n; i++) {
            char c = sc.next().toCharArray()[0];
            arr[c - 'a']++;
        }

        boolean flag = true;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= 5) {
                flag = false;
                System.out.print((char) (i + 'a'));
            }
        }
        if(flag) System.out.println("PREDAJA");

        sc.close();
    }
}
