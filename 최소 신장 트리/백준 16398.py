import sys
input = sys.stdin.readline

n = int(input())

def find_parents(parents, x) :
    if parents[x] != x :
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, a, b) :
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b :
        parents[b] = a
    else :
        parents[a] = b

parents = [0] * (n + 1)
for i in range(n + 1) :
    parents[i] = i

costs = []
edges = []

for i in range(n) :
    costs.append(list(map(int, input().strip().split())))

for i in range(n) :
    for j in range(i) :
        edges.append((costs[i][j], i+1, j+1))

# print(edges)
edges.sort()

answer = 0
for edge in edges :
    cost, a, b = edge
    if find_parents(parents, a) != find_parents(parents, b) :
        answer += cost
        union_parents(parents, a, b)

print(answer)


