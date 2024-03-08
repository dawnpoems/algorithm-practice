import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
def backtracking(depth) :
    global N
    global M
    if depth == M :
        print(" ".join(map(str, lst)))
        return
    for i in range(1, N + 1) :
        lst.append(i)
        backtracking(depth + 1)
        lst.pop()

for i in range(1, N + 1) :
    lst.append(i)
    backtracking(1)
    lst.pop()