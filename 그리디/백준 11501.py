import sys
input = sys.stdin.readline

t_case = int(input())


for t in range(t_case) :
    n = int(input())
    prices = list(map(int, input().strip().split()))

    max_price = 0
    cnt = 0

    while prices :
        now = prices.pop()
        if now > max_price :
            max_price = now
        else :
            cnt += max_price - now

    print(cnt)