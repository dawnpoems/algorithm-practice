from collections import deque
import sys

node_num, edge_num, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(node_num + 1)]
edges = []
for i in range(edge_num):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
for i in graph:
    i.sort()

# 재귀로 dfs구현


def dfs(graph, node, visited):
    visited[node] = True  # 방문한 노드 True로 바꾸고 출력
    print(node, end=" ")

    for i in graph[node]:  # 주변 노드 탐색
        if not visited[i]:  # 아직 방문하지 않았으면
            dfs(graph, i, visited)  # 바로 탐색

# bfs 구현


def bfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True  # 첫 노드 큐에 넣고 방문으로 변경

    while queue:
        a = queue.popleft()
        print(a, end=" ")  # 큐에서 꺼내면서 출력
        for i in graph[a]:  # 연결된 노드 점검
            if not visited[i]:  # 아직 큐에 넣은적이 없으면
                queue.append(i)  # 큐에 추가
                visited[i] = True  # 큐에 넣은건 True로


dfs_visited = [False] * (node_num + 1)
bfs_visited = [False] * (node_num + 1)
# 방문 여부를 나타낸 리스트

dfs(graph, start, dfs_visited)
print()
bfs(graph, start, bfs_visited)
