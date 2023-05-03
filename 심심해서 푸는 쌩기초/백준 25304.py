import sys
cost = int(sys.stdin.readline())
n = int(sys.stdin.readline())

answer = 0
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    answer += (a*b)

if cost == answer:
    print("Yes")
else:
    print("No")