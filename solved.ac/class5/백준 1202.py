import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []

for i in range(N) :
    m, v = map(int, input().split())
    jewels.append((m, v))

jewels.sort()

bags = []
for i in range(K) :
    bags.append(int(input()))

bags.sort()
bags_can = [[] for _ in range(K)]

i = 0
for weight, price in jewels :
    while i < K and bags[i] < weight :
        i += 1
    if i >= K :
        break
    bags_can[i].append(price)

ans = 0
heap = []
for can in bags_can :
    for c in can :
        heapq.heappush(heap, -c)
    if heap :
        ans -= heapq.heappop(heap)
print(ans)
