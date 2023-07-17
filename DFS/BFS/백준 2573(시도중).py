import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

board = []

for i in range(n) :
    board.append(list(map(int, input().split())))

def melt(i, j, n, m, new_board) :
    if i - 1 >= 0 and board[i-1][j] == 0 :
        new_board[i][j] -= 1
    if i + 1 < n and board[i+1][j] == 0 :
        new_board[i][j] -= 1
    if j - 1 >= 0 and board[i][j-1] == 0 :
        new_board[i][j] -= 1
    if j + 1 < m and board[i][j+1] == 0 :
        new_board[i][j] -= 1

    if new_board[i][j] < 0 :
        new_board[i][j] = 0

def dfs(r, c, n, m) :
    if r < 0 or r >= n or c < 0 or c >= m :
        return False

    if board[r][c] != 0 and not visited[r][c] :
        visited[r][c] = True
        melt(r, c, n, m, new_board)

        dfs(r + 1, c, n, m)
        dfs(r - 1, c, n, m)
        dfs(r, c + 1, n, m)
        dfs(r, c - 1, n, m)
        return True
    return False


time = 0

new_board = copy.deepcopy(board)

while True :
    visited = [[False] * m for _ in range(n)]
    pieces = []
    end_flag = True
    start = [0, 0]

    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 :
                visited[i][j] = True
            else :
                end_flag = False
                start = [i, j]
    
    dfs(start[0], start[1], n, m)
                


    # print("-------")

    # for row in board :
    #     print(" ".join(map(str, row)))
    
    # print(">")
    # for row in new_board :
    #     print(" ".join(map(str, row)))
    

    # print(start)
    # print(visited)

    if end_flag :
        print(0)
        break

    if any(False in l for l in visited) :
        print(time)
        break

    time += 1
    board = copy.deepcopy(new_board)

#힌트 퍼온거

#첫번째 행과 열, 마지막 행과 열은 무조건 바다이므로 bfs 든 dfs든 탐색에서 제외합니다.

#빙산이 나누어져있는지 검사할때 탐색함수를 두번돌면 무조건 빙산이 나누어진것이므로

#for문이 끝날때까지 기다리는 것이 아니라 두번째 탐색하려고 진입하는 순간 true를 리턴하고 함수를 종료 시킵니다.

#감소시키는 decrease함수도 따로만드는 것이아니라 bfs함수를 돌면서 빙산 주위의 바다개수를 구하여 저장한뒤 모든 탐색이 끝난 후

#바다 개수만큼 빙산 높이를 낮춰주었습니다.


#여기서 for문을 이용하여 x+1,x-1,y+1,y-1을 탐색하는 것보다 if문을 이용하는게 더 빠릅니다.