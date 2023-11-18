import java.util.*;

public class Bk_10988 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        char[] charArray = word.toCharArray();
        System.out.println(isPalindrome(charArray) ? 1 : 0);
    }

    public static boolean isPalindrome(char[] charArray) {
        for (int i = 0; i < charArray.length / 2; i++) {
            if(charArray[i] != charArray[charArray.length - 1 - i]) {
                return false;
            }
        }
        return true;
    }
}
