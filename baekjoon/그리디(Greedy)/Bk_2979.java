import java.util.Scanner;

public class Bk_2979 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int[] arr = new int[101];
        int sum = 0;
        for (int i = 0; i < 3; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();

            for (int j = start; j < end; j++) {
                arr[j]++;
            }
        }

        for (int i : arr) {
            if (i == 1) {
                sum += a;
            } else if (i == 2) {
                sum += b * 2;
            } else if (i == 3) {
                sum += c * 3;
            }
        }
        System.out.println(sum);
    }
}
