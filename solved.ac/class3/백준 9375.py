import sys
input = sys.stdin.readline

tc = int(input())

for t in range(tc) :
    dic = {}
    n = int(input())
    cnt = 1
    for i in range(n) :
        cloth, kind = input().split()
        if kind in dic :
            dic[kind] += 1
        else :
            dic[kind] = 1
    for val in dic.values() :
        cnt *= (val + 1)
    print(cnt - 1)