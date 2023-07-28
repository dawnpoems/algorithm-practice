import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for i in range(n) :
    board.append(list(map(int, list(input().strip()))))

#안부수고 왔으면 True로 바꿔주기.
visited = [[[-1, False] for j in range(m)] for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#세번째는 벽을 한번 부셨는지 여부
#네번째는 지금 얼마나 왔는지
queue = deque([(0, 0, False, 1)])
visited[0][0][0] = 1

while queue :
    r, c, brock, route = queue.popleft()
    # print(r, c, brock, route)
    for i in range(4) :
        row = r + dr[i]
        col = c + dc[i]
        if row < 0 or row >= n or col < 0 or col >= m :
            continue
        if brock :
            if board[row][col] == 0 and visited[row][col][0] == -1:
                visited[row][col][0] = route + 1
                queue.append((row, col, brock, route + 1))
        else :
            #벽 안부수고 온 적 있으면 넘어가기
            if visited[row][col][1] == True :
                continue
            
            #처음 온 곳이면 업데이트
            if visited[row][col][0] == -1 :
                visited[row][col][0] = route + 1
            
            #벽 안부수고 왔으니 왔다고 업데이트
            visited[row][col][1] = True

            #벽이면 brock변경해서 넘기기
            if board[row][col] == 1 :
                queue.append((row, col, True, route + 1))
            else :
                queue.append((row, col, False, route + 1))
            

print(visited[n-1][m-1][0])
