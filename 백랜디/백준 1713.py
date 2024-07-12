import sys, heapq
input = sys.stdin.readline

N = int(input())

K = int(input())

frames = []

nums = list(map(int, input().split()))

for k in range(K) :
    frame_nxt = []
    dup = False
    while frames :
        cnt, order, num = heapq.heappop(frames)
        if num == nums[k] :
            dup = True
            cnt += 1
        heapq.heappush(frame_nxt, (cnt, order, num))
    frames = frame_nxt
    if not dup :
        if len(frames) < N :
            heapq.heappush(frames, (1, k, nums[k]))
        else :
            heapq.heappop(frames)
            heapq.heappush(frames, (1, k, nums[k]))
    # print(frames)

ans = []
while frames :
    cnt, order, num = heapq.heappop(frames)
    ans.append(num)

print(*sorted(ans))