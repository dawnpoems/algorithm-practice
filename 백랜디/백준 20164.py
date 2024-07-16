import sys
input = sys.stdin.readline

N = int(input())

# 새로운 수에서 숫자를 세고 cnt까지 넘겨줘야 함.
# 최종적으로 한자리 수가 되면, 답을 업데이트하기

ans_mx = 0
ans_mn = int(1e9)

def backtracking(now, cnt) :
    global ans_mx
    global ans_mn
    
    # 홀수 세기
    tmp = now
    while tmp :
        if (tmp % 10) % 2 == 1 :
            cnt += 1
        tmp //= 10

    if now < 10 :
        ans_mx = max(ans_mx, cnt)
        ans_mn = min(ans_mn, cnt)
        return

    if now < 100 :
        backtracking(now // 10 + now % 10, cnt)
    else :
        lst = []
        while now :
            lst.append(now % 10)
            now //= 10
        lst.reverse()
        for i in range(1, len(lst) - 1) : #두번째가 시작하는 위치
            for j in range(i + 1, len(lst)) : #세번째가 시작하는 위치
                idx = 0
                one = 0
                two = 0
                three = 0
                while idx < i :
                    one = one * 10 + lst[idx]
                    idx += 1
                while idx < j :
                    two = two * 10 + lst[idx]
                    idx += 1
                while idx < len(lst) :
                    three = three * 10 + lst[idx]
                    idx += 1
                backtracking(one + two + three, cnt)

backtracking(N, 0)

print(ans_mn, ans_mx)
                    