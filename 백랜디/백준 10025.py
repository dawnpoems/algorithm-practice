import sys
input = sys.stdin.readline

N, K = map(int, input().split())

max_pos = 1000000
ices = [0] * (max_pos + 1)
for i in range(N) :
    g, x = map(int, input().split())
    ices[x] = g

ans = 0
total = 0
for i in range(K) :
    if i <= max_pos :
        total += ices[i]

for i in range(max_pos + 1) :
    if i - K - 1 >= 0 :
        total -= ices[i - K - 1]
    if i + K <= max_pos :
        total += ices[i + K]
    ans = max(ans, total)

print(ans)