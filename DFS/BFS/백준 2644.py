import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

x, y = map(int, input().strip().split())

m = int(input())

graph = [[] for _ in range(n + 1)]

count_list = [-1] * (n + 1)

for i in range(m) :
    one, two = map(int, input().strip().split())
    graph[one].append(two)
    graph[two].append(one)

queue = deque([x])
count_list[x] = 0

found = False

count = 0
while queue :
    v = queue.popleft()
    if v == y :
        found = True
        print(count_list[v])
        break
    for i in graph[v] :
        if count_list[i] == -1 :
            queue.append(i)
            count_list[i] = count_list[v] + 1

if not found :
    print(-1)
