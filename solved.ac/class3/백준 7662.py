import sys, heapq
input=sys.stdin.readline

T = int(input())

for t in range(T) :
    heap_max = []
    heap_d_max = []
    heap_min = []
    heap_d_min = []
    k = int(input())
    for i in range(k) :
        oper, n = input().split()
        if (oper == "I") :
            heapq.heappush(heap_min, int(n))
            heapq.heappush(heap_max, (-1) * int(n))
        if (oper == "D" and n == "1") :
            while heap_max and heap_d_max :
                if heap_max[0] == heap_d_max[0] :
                    heapq.heappop(heap_max)
                    heapq.heappop(heap_d_max)
                else :
                    break 
            if heap_max :
                heapq.heappush(heap_d_min, -heapq.heappop(heap_max))
        if (oper == "D" and n == "-1") :
            while heap_min and heap_d_min :
                if heap_min[0] == heap_d_min[0] :
                    heapq.heappop(heap_min)
                    heapq.heappop(heap_d_min)
                else :
                    break
            if heap_min :
                heapq.heappush(heap_d_max, -heapq.heappop(heap_min))
    ans = []
    while heap_max and heap_d_max:
        if (heap_max[0] == heap_d_max[0]) :
            heapq.heappop(heap_max)
            heapq.heappop(heap_d_max)
        else :
            break
    if heap_max :
        ans.append(-heap_max[0])
    while heap_min and heap_d_min :
        if (heap_min[0] == heap_d_min[0]) :
            heapq.heappop(heap_min)
            heapq.heappop(heap_d_min)
        else :
            break
    if heap_min :
        ans.append(heap_min[0])
    else :
        if ans :
            ans.append(ans[0])
    if ans :
        print(ans[0], ans[1])
    else :
        print("EMPTY")
