import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m) :
    s, e, d = map(int, input().split())
    graph[s][e] = d

answer = INF
for k in range(1, n+1) :
    for s in range(1, n+1) :
        for e in range(1, n+1) :
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])
            if s == e :
                if answer > graph[s][e] :
                    answer = graph[s][e]

if answer == INF :
    print(-1)
else :
    print(answer)

# print("--------")
# for i in range(1, n + 1) :
#     for j in range(1, n + 1) :
#         print(graph[i][j], end=" ")
#     print()
# print("---------")