import sys
input = sys.stdin.readline

x, y, c = map(float, input().split())

def bi_search(start, end) :
    ans = 0
    while start + 0.001 <= end :
        wid = (start + end) / 2
        h1 = (x ** 2 - wid ** 2) ** 0.5
        h2 = (y ** 2 - wid ** 2) ** 0.5
        now = (h1 * h2) / (h1 + h2)
        if now >= c :
            ans = wid
            start = wid
        else :
            end = wid
    return ans

print(bi_search(1, min(x, y)))