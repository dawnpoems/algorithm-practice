import sys, math
from itertools import combinations
input = sys.stdin.readline

def find_parents(parents, x) :
    if parents[x] != x :
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b) :
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b :
        parents[b] = a
    else :
        parents[a] = b

n = int(input())

nodes = [0]
for i in range(n) :
    x, y = map(float, input().split())
    nodes.append((x, y))

parents = [0] * (n + 1)
for i in range(1, n + 1) :
    parents[i] = i

comb = combinations([i for i in range(1, n+1)], 2)

# print(nodes)
edges = []
for c in comb :
    a, b = c
    x1, y1 = nodes[a]
    x2, y2 = nodes[b]
    cost = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    edges.append((cost, a, b))

# print(edges)

edges.sort()

answer = 0
for edge in edges :
    cost, a, b = edge
    if find_parents(parents, a) != find_parents(parents, b) :
        union_parent(parents, a, b)
        answer += cost

print(round(answer, 2))