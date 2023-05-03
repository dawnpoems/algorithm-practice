# 전체 0으로 시작해서
# 거리를 숫자로 넣으면 될거같은데
# 전체 그냥 점검해버리고, 원하는 값 출력하면 될듯


from collections import deque
import sys


# 이동할 방향 정의
dx = [-2, -2, -1, -1, +1, +1, +2, +2]
dy = [+1, -1, +2, -2, +2, -2, +1, -1]


def bfs(board, start, end):
    if start == end:
        return 0  # 같은 장소면 그냥 반환
    queue = deque([[start[0], start[1]]])  # 첫 노드 큐에 넣기

    while queue:
        x, y = map(int, queue.popleft())
        for i in range(8):  # 전체 8곳 체크
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
                continue

            if board[nx][ny] == 0:  # 0이면(아직 안간곳)
                queue.append([nx, ny])  # 큐에 추가
                board[nx][ny] = board[x][y] + 1  # 큐에 넣은건 숫자 바꾸기
    board[start[0]][start[1]] = 0
    return board[end[0]][end[1]]  # 거리 반환


n = int(sys.stdin.readline())
for i in range(n):
    l = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))
    board = [[0] * l for _ in range(l)]
    print(bfs(board, start, end))
