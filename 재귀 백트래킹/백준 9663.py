import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
total = 0
table = [0] * n

def is_valid(row, col) :
    for r in range(row) :
        if table[r] == col or (row - r) == abs(table[r] - col) :
            return False
    return True

def dfs(n, row, col) :
    global total
    table[row] = col
    if row + 1 == n :
        total += 1
        return
    for i in range(n) :
        if is_valid(row + 1, i) :
            dfs(n, row + 1, i)

for i in range(n) :
    dfs(n, 0, i)

print(total)