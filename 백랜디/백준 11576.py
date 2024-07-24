import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

M = int(input())

num = list(map(int, input().split()))

ans = []

ten = 0
for i in range(M) :
    ten *= A
    ten += num[i]

while ten :
    ans.append(ten % B)
    ten //= B

while ans :
    print(ans.pop(), end=" ")