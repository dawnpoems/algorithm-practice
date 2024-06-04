import sys
input = sys.stdin.readline

while True :
    N = int(input())
    if N == 0 :
        break
    nums = [True] * (2 * N + 1)
    cnt = 0
    for i in range(2, 2 * N + 1) :
        if not nums[i] :
            continue
        if i > N :
            cnt += 1
        now = 2 * i
        while now <= 2 * N :
            nums[now] = False
            now += i
    print(cnt)