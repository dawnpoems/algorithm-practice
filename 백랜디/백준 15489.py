import sys
input = sys.stdin.readline


tri = [[0] * 31 for _ in range(31)]

tri[1][1] = 1

for i in range(2, 31) :
    for j in range(1, i + 1) :
        tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]

R, C, W = map(int, input().split())

ans = 0
for i in range(W) :
    for j in range(C, C + i + 1) :
        ans += tri[R + i][j]

print(ans)
