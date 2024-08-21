import sys
input = sys.stdin.readline

N = int(input())

guitars = []

for i in range(N) :
    guitars.append(input().strip())

def sort_cri(item) :
    total = 0
    for c in item :
        if c.isdigit() :
            total += int(c)
    return (len(item), total, item)

guitars.sort(key=sort_cri)

for g in guitars :
    print(g)

