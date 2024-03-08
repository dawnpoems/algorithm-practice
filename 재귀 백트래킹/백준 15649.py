import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
def backtracking(now, depth) :
    global N
    global M
    if depth == M :
        print(" ".join(map(str, lst)))
        return
    for i in range(1, N + 1) :
        if i not in lst :
            lst.append(i)
            backtracking(i, depth + 1)
            lst.pop()

for i in range(1, N + 1) :
    lst.append(i)
    backtracking(i, 1)
    lst.pop()