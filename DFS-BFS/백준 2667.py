import sys
input = sys.stdin.readline

n = int(input())

maps = []
for i in range(n) :
    maps.append(list(map(int, list(input().strip()))))

homes_count = []

count = 0

def dfs(x, y) : 
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    else :
        if maps[x][y] == 1 :
            global count
            count += 1
            maps[x][y] = 0
            dfs(x + 1, y)
            dfs(x -1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return True

for i in range(n) :
    for j in range(n) :
       if dfs(i, j) :
           homes_count.append(count)
           count = 0

print(len(homes_count))
homes_count.sort()
for home in homes_count :
    print(home)

