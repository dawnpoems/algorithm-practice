import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]

for i in range(m) :
    lines = list(map(int, input().strip().split()))

    for j, line in enumerate(lines) :
        if j == 0 :
            singer_cnt = line
        elif j < singer_cnt :
            graph[line].append(lines[j+1])
            indegree[lines[j+1]] += 1

# print(indegree)
def topology() :
    result = []
    queue = deque([])
    for i in range(1, n + 1) :
        if indegree[i] == 0 :
            queue.append(i)
    
    while queue :
        now = queue.popleft()
        result.append(now)
        for i in graph[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                queue.append(i)
    return result

answer = topology()
# print(answer)
if len(answer) < n :
    print(0)
else :
    for ans in answer :
        print(ans)