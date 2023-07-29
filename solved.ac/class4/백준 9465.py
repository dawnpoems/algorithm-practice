import sys
input = sys.stdin.readline

tc = int(input())


for t in range(tc) :
    n = int(input())
    stickers = []
    for i in range(2) :
        stickers.append(list(map(int, input().strip().split())))
    
    d = [[0] * (n + 1) for _ in range(2)]

    for i in range(n) :
        if i == 0 :
            d[0][i] = stickers[0][0]
            d[1][i] = stickers[1][0]
        elif i == 1 :
            d[0][i] = stickers[0][1] + stickers[1][0]
            d[1][i] = stickers[0][0] + stickers[1][1]
        else :
            d[0][i] = max(d[1][i-2] + stickers[0][i], d[1][i-1] + stickers[0][i])
            d[1][i] = max(d[0][i-2] + stickers[1][i], d[0][i-1] + stickers[1][i])
        # print("---------")
        # print(d)
    print(max(map(max, d)))

        





