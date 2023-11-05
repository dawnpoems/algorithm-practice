import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m) :
    a, b = map(int, input().split())
    if b not in graph[a] :
        graph[a].append(b)
    if a not in graph[b] :
        graph[b].append(a)

# 본인을 제외한 모두에게 가는 최단거리 중에서
# 가장 큰케 케빈 베이컨이네
#DFS나 BFS로 전체 탐색하고, 최댓값 구하면 될듯.

def bfs(start) :
    queue = deque([start])
    board[start] = 0
    while (queue) :
        now = queue.popleft()
        for j in graph[now] :
            if board[now] + 1 < board[j] :
                board[j] = board[now] + 1
                queue.append(j)

kb_idx = 0
kb_min = 1e9

for i in range(1, n + 1) :
    board = [1e9] * (n + 1)
    board[0] = 0
    bfs(i)
    kb = sum(board)
    if kb < kb_min :
        kb_idx = i
        kb_min = kb

print(kb_idx)

