import sys
input = sys.stdin.readline

tc = int(input())

table = [0] * 101

table[1] = table[2] = table[3] = 1
table[4] = table[5] = 2

#점화식 : f(n) = f(n-1) + f(n-5)

for t in range(tc) :
    n = int(input())
    if n <= 5 :
        print(table[n])
    else :
        for i in range(6, n + 1) :
            table[i] = table[i-1] + table[i-5]
        # print(table)
        print(table[n])

