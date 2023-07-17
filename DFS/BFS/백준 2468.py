import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

spaces = []
spaces_set = [0]

for i in range(n) :
    row = list(map(int, input().split()))
    for num in row :
        if num not in spaces_set :
            spaces_set.append(num)
    spaces.append(row)

def dfs(r, c) : 
    if r < 0 or r >= n or c < 0 or c >= n :
        return False

    if visited[r][c] == 0 :
        visited[r][c] = 1
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        return True
    
    return False
max_answer = 0

for h in spaces_set :
    answer = 0
    visited = [[0]* n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if spaces[i][j] <= h :
                visited[i][j] = 2

    for i in range(n) :
        for j in range(n) :
            if dfs(i, j) :
                answer += 1
    if answer > max_answer :
        max_answer = answer
    # print(answer)
    # print(visited)

print(max_answer)
