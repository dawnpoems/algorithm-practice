import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

items = [0]

items.extend(list(map(int, input().strip().split())))

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1) :
    for j in range(1, n+1) :
        if i==j :
            graph[i][j] = 0

for i in range(r) :
    s, e, d = map(int, input().split())
    if graph[s][e] > d :
        graph[s][e] = d
    if  graph[e][s] > d :
        graph[e][s] = d

for k in range(1, n+1) :
    for s in range(1, n + 1) :
        for e in range(1, n+1) :
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

# print("--------")
# for i in range(1, n + 1) :
#     for j in range(1, n + 1) :
#         print(graph[i][j], end=" ")
#     print()
# print(items)
# print("---------")
answers = []
for s in range(1, n + 1) :
    cnt = 0
    for e in range(1, n + 1) :
        if graph[s][e] <= m :
            cnt += items[e]
    answers.append(cnt)

# print(answers)
print(max(answers))