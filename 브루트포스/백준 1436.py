import sys
input = sys.stdin.readline

n = int(input())
cnt = 666
ans_num = 0

while ans_num < n :
    now = cnt
    six = 0
    while now > 0 :
        space = now % 10
        now = now // 10
        if space == 6 :
            six += 1
        else :
            six = 0
        if six == 3 :
            ans_num += 1
            break
    cnt += 1

print(cnt - 1)