import sys
sys.stdin = open('1018.txt')

input = sys.stdin.readline

N = 8
str1 = "WBWBWBWB"
str2 = "BWBWBWBW"
pivot1 = [str1, str2, str1, str2, str1, str2, str1, str2]
pivot2 = [str2, str1, str2, str1, str2, str1, str2, str1]

a, b = [int(x) for x in input().rstrip().split()]
arr = [input().rstrip() for _ in range(a)]

rst = 10000
for i in range(a-N + 1):
    for j in range(b-N + 1):
        count = 0
        for p in range(N):
            for q in range(N):
                if arr[i+p][j+q] != pivot1[p][q]:
                    count += 1

        rst = min(rst, count)
        count = 0
        for p in range(N):
            for q in range(N):
                if arr[i+p][j+q] != pivot2[p][q]:
                    count += 1
        rst = min(rst, count)
print(rst)
