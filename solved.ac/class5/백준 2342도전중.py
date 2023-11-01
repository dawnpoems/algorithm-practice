import sys, heapq
input = sys.stdin.readline

route = list(map(int, input().strip().split()))
route.pop()
# print(route)

INF = int(1e9)
d = [[[INF] * 5 for _ in range(5)] for _ in range(len(route))]

#d[이동횟수][현재왼발][현재오른발]

def cal_cost(start, end) :
    if start == end :
        return 1
    elif start == 0 :
        return 2
    elif start == 1 and end == 3 :
        return 4
    elif start == 2 and end == 4 :
        return 4
    else :
        return 3
    
queue = []
# 에너지 총량, 현재왼발, 현재오른발, 이동횟수
heapq.heappush(queue, (2, route[0], 0, 1))
heapq.heappush(queue, (2, 0, route[0], 1))
while queue :
    # print(queue)
    energy, left, right, cnt = heapq.heappop(queue)
    
    if d[cnt-1][left][right] != INF :
        continue
    
    d[cnt-1][left][right] = energy

    if cnt < len(route) :
        nxt = route[cnt]
        #왼발이동
        heapq.heappush(queue, (energy + cal_cost(left, nxt), nxt, right, cnt + 1))
        #오른발이동
        heapq.heappush(queue, (energy + cal_cost(right, nxt), left, nxt, cnt + 1))


# print(d)
# print(d[-1])
print(min(map(min, d[-1])))