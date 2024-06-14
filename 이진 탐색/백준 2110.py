import sys

N, C = map(int, sys.stdin.readline().split())

homes = []

for i in range(N):
    homes.append(int(sys.stdin.readline()))

homes.sort()

def can_install(k) :
    global C
    before = homes[0]
    i = 1
    cnt = 1
    while i < len(homes) :
        if homes[i] - before >= k :
            cnt += 1
            before = homes[i]
            if cnt >= C :
                return True
        i += 1
    return False

def bi_search(start, end) :
    ans = 0
    while start <= end :
        mid = (start + end) // 2
        if can_install(mid) :
            ans = mid
            start = mid + 1
        else :
            end = mid - 1
    return ans

print(bi_search(0, 10 ** 9))