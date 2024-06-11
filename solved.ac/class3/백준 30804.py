import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))
tanghulu = deque([])
kinds = [0] * 10

cnt = 0
ans = 0

for f in fruits :
    if kinds[f] == 0 :
        cnt += 1
    kinds[f] += 1
    tanghulu.append(f)
    while cnt > 2 :
        now = tanghulu.popleft()
        kinds[now] -= 1
        if kinds[now] <= 0 :
            cnt -= 1
    ans = max(ans, len(tanghulu))
        
print(ans)
