import sys
input = sys.stdin.readline

n = int(input())

drinks = []
d = [0] * (n + 1)

for i in range(1, n + 1) :
    dri = int(input())
    if i == 1 :
        d[i] = dri
    elif i == 2 :
        d[i] = d[1] + dri
    else :
        d[i] = max(d[i-1], d[i-2] + dri, d[i-3] + drinks[-1] + dri)
    drinks.append(dri)

# print(drinks)
# print(d)
print(max(d))
