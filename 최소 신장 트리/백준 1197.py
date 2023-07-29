import sys
input = sys.stdin.readline

v, e = map(int, input().split())

edges = []
for i in range(e) :
    s, e, d = map(int, input().split())
    edges.append((d, s, e))

edges.sort()

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

parents = [0] * (v + 1)
for i in range(1, v + 1) :
    parents[i] = i 

answer = 0
for edge in edges :
    cost, a, b = edge
    if find_parents(parents, a) != find_parents(parents, b) :
        union_parents(parents, a, b)
        answer += cost

# print(parents)
# print(edges)
print(answer)