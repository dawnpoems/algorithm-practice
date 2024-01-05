import sys, heapq
input = sys.stdin.readline

n = int(input())

plus_heap = []
minus_heap = []

for i in range(n) :
    now = int(input())
    if now == 0 :
        print("answer : ", end="")
        if len(plus_heap) + len(minus_heap) == 0 :
            print(0)
        elif (len(plus_heap) == 0) :
            print(-heapq.heappop(minus_heap))
        elif (len(minus_heap) == 0) :
            print(heapq.heappop(plus_heap))
        else :
            p = heapq.heappop(plus_heap)
            m = heapq.heappop(minus_heap)
            if (p < m) :
                print(p)
                heapq.heappush(minus_heap, m)
            else :
                print(-m)
                heapq.heappush(plus_heap, p)
    else :
        if (now > 0) :
            heapq.heappush(plus_heap, now)
        else :
            heapq.heappush(minus_heap, -now)
    print(plus_heap, end=" ")
    print(minus_heap)