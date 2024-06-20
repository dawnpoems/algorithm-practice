import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = []

for i in range(R) :
    board.append(list(input().strip()))
    
road = [0] * 26
ans = 0
road_cnt = 0
def backtraking(r, c) :
    global R
    global C
    global ans
    global road_cnt
    idx = ord(board[r][c]) - 65
    if road[idx] :
        return
    road_cnt += 1
    road[idx] = 1
    if r - 1 >= 0 :
        backtraking(r - 1, c)
    if c - 1 >= 0 :
        backtraking(r, c - 1)
    if r + 1 < R :
        backtraking(r + 1, c)
    if c + 1 < C :
        backtraking(r, c + 1)
    if ans < road_cnt :
        ans = road_cnt
    road_cnt -= 1
    road[idx] = 0

backtraking(0, 0)
print(ans)