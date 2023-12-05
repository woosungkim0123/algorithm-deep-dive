import java.util.Scanner;

public class Bk_10808 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        
        int[] arr = new int[26];

        char[] chars = word.toCharArray();

        for (char aChar : chars) {
            int result = (int) aChar - (int) 'a';
            arr[result]++;
        }
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
