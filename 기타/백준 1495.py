import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())

vols = list(map(int, input().split()))

visited = [[False] * (M + 1) for _ in range(N + 1)]

visited[0][S] = True

for i in range(1, N + 1) :
    for j in range(M + 1) :
        if j - vols[i - 1] >= 0 :
            if visited[i - 1][j - vols[i - 1]] :
                visited[i][j] = True
        if j + vols[i - 1] <= M :
            if visited[i - 1][j + vols[i - 1]] :
                visited[i][j] = True

ans = -1
for i in range(M, -1, -1) :
    if visited[N][i] :
        ans = i
        break
print(ans)