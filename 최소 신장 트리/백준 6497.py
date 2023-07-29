import sys
input = sys.stdin.readline

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

while True :
    n, m = map(int, input().split())
    if n == 0 and m == 0 :
        break
    parents = [0] * (n + 1)
    for i in range(1, n + 1) :
        parents[i] = i

    total = 0
    edges = []
    for i in range(m) :
        a, b, cost = map(int, input().split())
        total += cost
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges :
        cost, a, b = edge
        if find_parents(parents, a) != find_parents(parents, b) :
            union_parents(parents, a, b)
            total -= cost

    print(total)