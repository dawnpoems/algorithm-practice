import sys

input = sys.stdin.readline

n, m = map(int, input().split())

given_board = []
target_board1 = []
target_board2 = []

for i in range(4) :
    target_board1.append(["W", "B", "W", "B", "W", "B", "W", "B"])
    target_board1.append(["B", "W", "B", "W", "B", "W", "B", "W"])
    target_board2.append(["B", "W", "B", "W", "B", "W", "B", "W"])
    target_board2.append(["W", "B", "W", "B", "W", "B", "W", "B"])

num_list = []

for i in range(n) :
    given_board.append(list(input().strip()))

for i in range(n - 7) :
    for j in range(m - 7) :
        oneTwo = [0, 0]
        for x in range(8) :
            for y in range(8):
                if given_board[i+x][j+y] != target_board1[x][y] :
                    oneTwo[0] += 1
                if given_board[i+x][j+y] != target_board2[x][y] :
                    oneTwo[1] += 1
        num_list.append(min(oneTwo))

print(min(num_list))
