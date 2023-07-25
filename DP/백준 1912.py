import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().strip().split()))

# 점화식 max(f(n), f(n-1) + f(n))
d = [0] * n
d[0] = numbers[0]
for i in range(1, n) :
    d[i] = max(numbers[i], numbers[i] + d[i-1])

# print(d)
print(max(d))