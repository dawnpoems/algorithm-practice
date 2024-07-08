import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())

sour = []
bitter = []

for i in range(N) :
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)

ans = 10 ** 9
for i in range(1, N + 1) :
    comb = combinations(range(N), i)
    for co in comb :
        now_s = 1
        now_b = 0
        # print(co)
        for c in co :
            now_s *= sour[c]
            now_b += bitter[c]
        # print(now_s, now_b)
        ans = min(ans, abs(now_s - now_b))

print(ans)
