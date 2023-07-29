import sys
input = sys.stdin.readline

tc = int(input())

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
    
for t in range(tc) :
    n, m = map(int, input().split())

    parents = [0] * (n + 1)
    for i in range(1, n + 1) :
        parents[i] = i

    cnt = 0
    for i in range(m) :
        a, b = map(int, input().split())

        if find_parents(parents, a) != find_parents(parents, b) :
            cnt += 1
            union_parents(parents, a, b)
    print(cnt)