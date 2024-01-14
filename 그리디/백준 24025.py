import sys
input=sys.stdin.readline

N = int(input())

down = 1
up = N

no_flag = 0

A = list(map(int, input().split()))
rocks = []

for i in range(N) :
    if A[i] > 0 :
        rocks.append(up)
        up -= 1
    else :
        if (i == N - 1) :
            no_flag = 1
            break
        rocks.append(down)
        down += 1

if no_flag :
    print(-1)
else :
    print(" ".join(map(str, rocks)))