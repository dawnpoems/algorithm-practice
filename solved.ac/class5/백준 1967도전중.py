import sys
input = sys.stdin.readline

N = int(input())

lst = [[] for _ in range(N + 1)]

for i in range(N - 1) :
    parent, child, weight = map(int, input().split())
    lst[parent].append((child, weight))

print(lst)
best = 0
second = 0

def update_best(now) :
    global best
    global second
    if second < now :
        second = now
    if best < second :
        tmp = best
        best = second
        second = tmp
    print(best, second)
        
def dfs(now, depth) :
    if len(lst[now]) == 0 :
        update_best(depth)
        return
    for c in lst[now] :
        dfs(c[0], depth + c[1])

ans_lst = []

for i in range(1, N + 1) :
    best = 0
    second = 0
    dfs(i, 0)
    ans_lst.append(best + second)

print(ans_lst)