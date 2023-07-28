import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

m = max(n, k)
d = [int(1e9)] * (m*2 + 1)
d[n] = 0

queue = deque([n])

while queue :
    v = queue.popleft()
    front = v + 1
    if 0 <= front <= m * 2 and d[front] > d[v] + 1 :
        d[front] = d[v] + 1
        queue.append(front)
    back = v - 1
    if 0 <= back <= m * 2 and d[back] > d[v] + 1 :
        d[back] = d[v] + 1
        queue.append(back)
    twice = v * 2
    if 0 <= twice <= m * 2 and d[twice] > d[v] :
        d[twice] = d[v]
        queue.append(twice)
    # print(queue)

# print(d)
print(d[k])
