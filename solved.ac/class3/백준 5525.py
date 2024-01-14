import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input().strip())
io_flag = 1
io_score = 0
ans = 0
    
for s in S :
    if io_flag == 1 :
        if s == 'I' :
            io_score += 1
            io_flag = 0
        else :
            io_score = 0
    else :
        if s == 'O' :
            io_score += 1
            io_flag = 1
        else :
            io_score = 1
            io_flag = 0
    # print(s, end=" ")
    # print(io_score)
    if (io_score >= N * 2 + 1) :
        ans += 1
        # print("got!")
        io_score -= 2

# print("--------------")
print(ans)