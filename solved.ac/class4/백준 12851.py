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

poss = 0
def backtracking(position, time) :
    global poss
    if not time :
        poss += 1
        return
    if 0 <= position - 1 <= 100000 and times[position - 1] == time - 1 :
        backtracking(position - 1, time - 1)
    if 0 <= position + 1 <= 100000 and times[position + 1] == time - 1 :
        backtracking(position + 1, time - 1)
    if 0 <= position // 2 <= 100000 and position % 2 == 0 and times[position // 2] == time - 1 :
        backtracking(position // 2, time - 1)

backtracking(K, fastest)
print(poss)