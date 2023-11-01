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

cycle = False
number = 0

games = []
for i in range(m) :
    a, b = map(int, input().split())
    games.append((a, b))

for game in games :
    a, b = game
    number += 1
    if find_parents(parents, a) == find_parents(parents, b) :
        cycle = True
        break
    else :
        union_parents(parents, a, b)

if cycle :
    print(number)
else :
    print(0)



