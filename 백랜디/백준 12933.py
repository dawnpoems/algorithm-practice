import sys
input = sys.stdin.readline

sound = list(input().strip())

visited = [False] * len(sound)

quack = "quack"

ans = 0

while True :
    # print(ans, visited)
    found = False
    idx = 0
    i_lst = []
    for i in range(len(sound)) :
        if not visited[i] and quack[idx] == sound[i] :
            i_lst.append(i)
            idx += 1
        if idx >= 5 :
            idx = 0
            found = True
            while i_lst :
                visited[i_lst.pop()] = True
    if found :
        ans += 1
    else :
        break

if False not in visited:
    print(ans)
else :
    print(-1)