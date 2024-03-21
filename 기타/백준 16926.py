import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

def rotate_square(r_start, r_end, c_start, c_end) :
    r = r_start
    while r <= r_end :
        if r + 1 > r_end :
            after[r][c_start + 1] = board[r][c_start]
        else :
            after[r + 1][c_start] = board[r][c_start]
        if r - 1 < r_start :
            after[r][c_end - 1] = board[r][c_end]
        else :
            after[r - 1][c_end] = board[r][c_end]
        r += 1
    c = c_start
    while c <= c_end :
        if c + 1 > c_end :
            after[r_end - 1][c] = board[r_end][c]
        else :
            after[r_end][c + 1] = board[r_end][c]
        if c - 1 < c_start :
            after[r_start + 1][c] = board[r_start][c]
        else :
            after[r_start][c - 1] = board[r_start][c]
        c += 1

def just_copy(r_start, r_end, c_start, c_end) :
    r = r_start
    while r <= r_end :
        after[r][c_start] = board[r][c_start]
        after[r][c_end] = board[r][c_end]
        r += 1
    c = c_start
    while c <= c_end :
        after[r_start][c] = board[r_start][c]
        after[r_end][c] = board[r_end][c]
        c += 1

rot_nums = []
for i in range(min(N, M) // 2) :
    rot_nums.append(R % ((N - i * 2 + M - i * 2) * 2 - 4))

while True :
    flag = 0
    after = [[0] * M for _ in range(N)]
    for j in range(len(rot_nums)) :
        if rot_nums[j] > 0 :
            rotate_square(j, N - j - 1 , j, M - j - 1)
            rot_nums[j] -= 1
            flag = 1
        else :
            just_copy(j, N - j - 1 , j, M - j - 1)
    if flag == 0 :
        break
    else :
        board = after

for k in range(N) :
    print(" ".join(map(str, after[k])))
