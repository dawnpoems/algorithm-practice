import sys, math
input = sys.stdin.readline

t = int(input())
for i in range(t) :
    M, N, x, y = map(int, input().split())
    k = x - 1
    found = 0
    while (k <= math.lcm(M, N)) :
        # print(k, end="")
        # print(k % M + 1, end=" ")
        # print(k % N + 1)
        if (k % N + 1 == y) :
            # print("answer : ", end="")
            print(k + 1)
            found = 1
            break
        k += M
    if not found :
        print(-1)
