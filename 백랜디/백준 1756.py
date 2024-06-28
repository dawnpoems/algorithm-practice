import sys, bisect
input = sys.stdin.readline

D, N = map(int, input().split())

oven = list(map(int, input().split()))

can_put = []

INF = 1e9
mn = INF
for i in range(D) :
    mn = min(mn, oven[i])
    can_put.append(mn)

can_put.reverse()
# print(can_put)
pizzas = list(map(int, input().split()))

top = -1
for pizza in pizzas :
    idx = bisect.bisect_left(can_put, pizza)
    if top >= idx :
        idx = top + 1
    print(idx)
    top = max(top, idx)
    if idx >= D :
        break

if top >= D :
    print(0)
else :
    print(D - top)
