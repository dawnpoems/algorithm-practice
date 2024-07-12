import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

from itertools import combinations

N, K, R = map(int, input().split())

roads = []

for i in range(R) :
    r1, c1, r2, c2 = map(int, input().split())
    roads.append(((r1, c1), (r2, c2)))

cows = []
for k in range(K) :
    r, c = map(int, input().split())
    cows.append((r, c))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_road(r1, c1, r2, c2) :
    for road in roads :
        if r1 == road[0][0] and c1 == road[0][1] and r2 == road[1][0] and c2 == road[1][1] :
            return True
        if r2 == road[0][0] and c2 == road[0][1] and r1 == road[1][0] and c1 == road[1][1] :
            return True
    return False

def dfs(r, c) :
    global cnt
    if visited[r][c] == 1 :
        return
    if visited[r][c] == -1 :
        cnt += 1
    visited[r][c] = 1
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 < nr <= N and 0 < nc <= N and is_road(r, c, nr, nc) == False :
            dfs(nr, nc)

ans = 0

visited = [[0] * (N + 1) for _ in range(N + 1)]

for cow in cows :
    visited[cow[0]][cow[1]] = -1

areas = []

for k in range(K) :
    cnt = 0
    dfs(cows[k][0], cows[k][1])
    if cnt :
        areas.append(cnt)

for comb in combinations(areas, 2) :
    ans += comb[0] * comb[1]

print(ans)