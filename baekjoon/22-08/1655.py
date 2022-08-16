# 틀림 힙써야한데
import heapq
import sys
sys.stdin = open('1655.txt')

# Let's keep the value of left root is the answer
cnt = int(sys.stdin.readline())
left, right = [], []

for i in range(cnt):
    num = int(sys.stdin.readline())

    # Fill in the numbers from the left
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    # Compare if left is bigger than right
    if i > 0 and left[0][1] > right[0][1]:
        temp_l = heapq.heappop(left)[1]
        temp_r = heapq.heappop(right)[1]
        heapq.heappush(left, (-temp_r, temp_r))
        heapq.heappush(right, (temp_l, temp_l))

    print(left[0][1])


# array = []

# for i in range(1, n + 1):

#     array.append(int(read()))
#     array.sort()
#     if i % 2 == 0:
#         print(array[(i // 2) - 1])
#     else:
#         print(array[(i // 2)])
