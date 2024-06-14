import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, K = map(int, input().split())

queue = deque([N])
times = [-1] * 100001
times[N] = 0

fastest = -1
while queue :
    now = queue.popleft()
    if now == K :
        fastest = times[now]
        break
    if 0 <= now - 1 <= 100000 and times[now - 1] == -1 :
        times[now - 1] = times[now] + 1
        queue.append(now - 1)
    if 0 <= now + 1 <= 100000 and times[now + 1] == -1 :
        times[now + 1] = times[now] + 1
        queue.append(now + 1)
    if 0 <= now * 2 <= 100000 and times[now * 2] == -1 :
        times[now * 2] = times[now] + 1
        queue.append(now * 2)

print(fastest)


ans = []
found = False
def backtracking(position, time) :
    global found
    if found :
        return
    ans.append(position)
    if not time :
        found = True
        return
    if 0 <= position - 1 <= 100000 and times[position - 1] == time - 1 :
        backtracking(position - 1, time - 1)
    if 0 <= position + 1 <= 100000 and times[position + 1] == time - 1 :
        backtracking(position + 1, time - 1)
    if 0 <= position // 2 <= 100000 and position % 2 == 0 and times[position // 2] == time - 1 :
        backtracking(position // 2, time - 1)
    if not found :
        ans.pop()

backtracking(K, fastest)
ans.reverse()
print(*ans)