import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dp = [-1] * (N + 1)
queue = deque([(1, 0)])

while queue :
    now = queue.popleft()
    if dp[now[0]] != -1 :
        continue
    # print(now)
    dp[now[0]] = now[1] 
    if dp[now[0]] == N :
        break
    if now[0] * 3 <= N :
        queue.append((now[0] * 3, now[0]))
    if now[0] * 2 <= N :
        queue.append((now[0] * 2, now[0]))
    if now[0] + 1 <= N :
        queue.append((now[0] + 1, now[0]))
    # print(queue)

now = N
ans = []
while now :
    ans.append(now)
    now = dp[now]

print(len(ans) - 1)
print(*ans)