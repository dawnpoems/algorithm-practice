import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

lst = [[] for _ in range(N + 1)]

for i in range(N - 1) :
    parent, child, weight = map(int, input().split())
    lst[parent].append((child, weight))
    lst[child].append((parent, weight))
        

ans = 0

def dfs(now, depth, start) :
    global ans
    visited[now] = True
    if now != start and len(lst[now]) == 1 :
        if ans < depth :
            ans = depth
        return
    for c in lst[now] :
        if not visited[c[0]] :
            dfs(c[0], depth + c[1], start)

for i in range(1, N + 1) :
    visited = [False] * (N + 1)
    if len(lst[i]) == 1 :
        dfs(i, 0, i)

print(ans)