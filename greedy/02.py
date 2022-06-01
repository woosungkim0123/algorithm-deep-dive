n = 5
m = 8
k = 3
data = [2, 4, 5, 4, 6]

data.sort()

print(data)
first = data[n - 1]
second = data[n - 2]

result = 0


# while True:
#    for i in range(k):
#       if m == 0:
#            break
#        result += first
#        m -= 1
#
#    if m == 0:
#        break
#    result += second
#    m -= 1

count = int(m / (k + 1)) * k
count += m % (k + 1)

result += count * first
result += (m-count) * second

print(result)
