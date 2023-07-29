import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if i == j :
            graph[i][j] = 0

for i in range(m) :
    s, e, d = map(int, input().split())
    if graph[s][e] > d :
        graph[s][e] = d

fri_cnt = int(input())

fri_cities = list(map(int, input().strip().split()))

for k in range(1, n+1) :
    for s in range(1, n+1) :
        for e in range(1, n+1) :
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

# print("--------")
# for i in range(1, n + 1) :
#     for j in range(1, n + 1) :
#         print(graph[i][j], end=" ")
#     print()
# print("---------")

answer_cnt = INF
answer = []
for i in range(1, n+1) :
    max_cnt = 0
    for city in fri_cities :
        now_cnt = graph[i][city] + graph[city][i]
        if now_cnt > max_cnt :
            max_cnt = now_cnt
    if answer_cnt == max_cnt :
        answer.append(i)
    elif answer_cnt > max_cnt :
        answer_cnt = max_cnt
        answer = [i]

# print(answer_cnt)
print(" ".join(map(str, answer)))