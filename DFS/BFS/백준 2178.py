from collections import deque
import sys

row, colunm = map(int, sys.stdin.readline().split())

miro = []

for i in range(row):
    miro.append(list(map(int, list(str(sys.stdin.readline().strip())))))

# 너비우선탐색 시작.


def bfs(miro, row, colunm):
    queue = deque([[0, 0]])
    miro[0][0] = 1  # 첫 노드 큐에 넣고 방문으로 변경
    distance = 1  # 거리 1에서 시작

    while queue:
        x, y = map(int, queue.popleft())
        graph = []
        if x - 1 >= 0:
            graph.append([x-1, y])
        if x + 1 < row:
            graph.append([x+1, y])
        if y - 1 >= 0:
            graph.append([x, y-1])
        if y + 1 < colunm:
            graph.append([x, y+1])
        for i in graph:  # 연결된 노드 점검
            if miro[i[0]][i[1]] == 1:  # 1이면
                queue.append(i)  # 큐에 추가
                miro[i[0]][i[1]] = miro[x][y] + 1  # 큐에 넣은건 숫자 바꾸기
    miro[0][0] = 1
    return miro[row-1][colunm-1]  # 거리 반환


print(bfs(miro, row, colunm))
