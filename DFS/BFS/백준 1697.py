import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque([(n)])

times = [-1] * 100001
times[n] = 0

while queue :
    v = queue.popleft()
    if v == k :
        print(times[v])
        break

    v1 = v - 1
    v2 = v + 1
    v3 = v * 2

    if 0 <= v1 <= 100000 and times[v1] == -1 :
        times[v1] = times[v] + 1
        queue.append(v1)
    if 0 <= v2 <= 100000 and times[v2] == -1 :
        times[v2] = times[v] + 1
        queue.append(v2)
    if 0 <= v3 <= 100000 and times[v3] == -1 :
        times[v3] = times[v] + 1
        queue.append(v3)

print(times[:30])