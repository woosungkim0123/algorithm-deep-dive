import java.util.Arrays;
import java.util.Scanner;

public class Bk_2309 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[9];
        int sum = 0;
        int spy1 = 0;
        int spy2 = 0;

        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
            sum += arr[i];
        }

        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (sum - arr[i] - arr[j] == 100) {
                    spy1 = i;
                    spy2 = j;
                    break;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            if (i == spy1 || i == spy2) {
                continue;
            }
            System.out.println(arr[i]);
        }
        sc.close();
    }
}