import sys
input = sys.stdin.readline

H, Y = map(int, input().split())

ans = 0

def backtracking(now, year) :
    global ans
    if year <= 0 :
        ans = max(ans, now)
        return
    if year - 5 >= 0 :
        backtracking(int(now * 1.35), year - 5)
    if year - 3 >= 0 :
        backtracking(int(now * 1.2), year - 3)
    if year - 1 >= 0 :
        backtracking(int(now * 1.05), year - 1)

backtracking(H, Y)

print(ans)