import sys
input = sys.stdin.readline

N = int(input())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

ans = 200 * N

lst_s = []
lst_l = []

def backtracking(now) :
    global N
    global ans
    if (len(lst_s) > N // 2 or len(lst_l) > N // 2) :
        return
    if (len(lst_s) == N // 2 and len(lst_l) == N // 2) :
        total_s = 0
        total_l = 0
        for i in range(1, N // 2) :
            for j in range(i) :
                total_s += board[lst_s[i]][lst_s[j]]
                total_s += board[lst_s[j]][lst_s[i]]
                total_l += board[lst_l[i]][lst_l[j]]
                total_l += board[lst_l[j]][lst_l[i]] 
        if (ans > abs(total_s - total_l)) :
            ans = abs(total_s - total_l)
    lst_s.append(now)
    backtracking(now + 1)
    lst_s.pop()
    lst_l.append(now)
    backtracking(now + 1)
    lst_l.pop()

backtracking(0)
print(ans)
