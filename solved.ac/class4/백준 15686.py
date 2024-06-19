import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

board = []
homes = []
stores = []

for i in range(N) :
    line = list(map(int, input().split()))
    for j in range(N) :
        if line[j] == 1 :
            homes.append((i, j))
        if line[j] == 2 :
            stores.append((i, j))
        
dists = [[0] * len(homes) for _ in range(len(stores))]

def get_dist(r1, c1, r2, c2) :
    return abs(r1 - r2) + abs(c1 - c2)

for i in range(len(stores)) :
    for j in range(len(homes)) :
        dists[i][j] = get_dist(stores[i][0], stores[i][1], homes[j][0], homes[j][1])

print(dists)

comb = combinations(range(len(stores)), M)

ans = 10 ** 9
for co in comb :
    print(co)
    now = 0
    for i in range(len(homes)) :
        m = 10 ** 9
        for c in co :
            m = min(m, dists[c][i])
        now += m
    ans = min(ans, now)

print(ans)

# 0번 home에서 0번으로 가는 거리, 1번으로 가는 거리 중 최솟값. -> now 에 더하기
