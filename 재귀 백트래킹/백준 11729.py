import sys
input = sys.stdin.readline

route = []

def hanoi(n, start, by, end) :
    if n == 0 :
        return
    hanoi(n - 1, start, end, by)
    route.append((start, end))
    hanoi(n - 1, by, start, end)

hanoi(int(input()), 1, 2, 3)
print(len(route))
for r in route :
    print(r[0], r[1])