import sys
input = sys.stdin.readline

N, D = map(int, input().split())

ans = 0
for i in range(1, N + 1) :
    now = i
    while now :
        if now % 10 == D :
            ans += 1
        now //= 10

print(ans)