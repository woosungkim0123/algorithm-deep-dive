package com.example.demo;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    /**
     * 책 n개 들어옴, 2개 묶음으로 들어오는데 쌓을 때는 묶음으로 쌓아야하고 팔때는 앞에 있는 걸 먼저 팜
     * n이 3이라면 1,1,2,2,3,3의 책이 있음 배치 경우의수는 6가지임 (11 22 33, 11 33 22 ...)
     * 주문이 들어오고 책을 꺼내는데 힘이드는데 맨위면 0, 112233이렇게 쌓여있을 때 2권을 빼내려면 2의 힘이 듬
     * 최소로 드는 힘을 구하라
     * 주문은 최대 100개
     */
    public static int n;
    public static int[] orderArr;
    public static int minPower = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Main.n = sc.nextInt(); // 3
        sc.nextLine();

        String line = sc.nextLine(); // 1 2 1 3 3 2
        Main.orderArr = Arrays.stream(line.split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        orderCheck();

        int[] bookArr = new int[n];
        for (int i = 1; i <= n; i++) {
            bookArr[i - 1] = i;
        }

        permute(bookArr, 0);
        System.out.println(minPower);
    }

    private static boolean orderCheck() {
        for (int i = 0; i < orderArr.length / 2; i += 2) {
            if (orderArr[i] != orderArr[i + 1]) {
                return false;
            }
        }
        return true;
    }

    private static void permute(int[] bookArr, int index) {
        if (index == bookArr.length) {
            int power = getPower(bookArr);
            minPower = Math.min(minPower, power);
        } else {
            for (int i = index; i < bookArr.length; i++) {
                swap(bookArr, index, i);
                permute(bookArr, index + 1);
                swap(bookArr, index, i);
            }
        }
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }

    private static int getPower(int[] bookArr) {
        int power = 0;
        int[] realBookArr = new int[bookArr.length * 2];

        for (int i = 0, j = 0; i < bookArr.length; i++) {
            realBookArr[j++] = bookArr[i];
            realBookArr[j++] = bookArr[i];
        }

        for (int order : orderArr) {
            for (int i = 0; i < realBookArr.length; i++) {
                if (realBookArr[i] == order) {
                    power += i;
                    int[] tempArr = new int[realBookArr.length - 1];
                    System.arraycopy(realBookArr, 0, tempArr, 0, i);
                    System.arraycopy(realBookArr, i + 1, tempArr, i, realBookArr.length - i - 1);
                    realBookArr = tempArr;
                    break;
                }
            }
        }
        return power;
    }
}
