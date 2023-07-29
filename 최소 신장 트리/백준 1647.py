import sys
input = sys.stdin.readline

n, m = map(int, input().split())

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
for i in range(1, n + 1) :
    parents[i] = i

edges = []
answer = 0
for i in range(m) :
    s, c, cost = map(int, input().split())
    edges.append((cost, s, c))

edges.sort()

min_edges = []
for edge in edges :
    cost, a, b = edge
    if find_parents(parents, a) != find_parents(parents, b) :
        union_parents(parents, a, b)
        answer += cost
        min_edges.append(edge)

print(answer - min_edges[-1][0])