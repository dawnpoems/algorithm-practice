import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []

for i in range(N) :
    nums.append(int(input()))

tree = [[int(1e9), 0] for _ in range(N * 4)]

def init(start, end, idx) :
    if start == end :
        tree[idx][0] = nums[start]
        tree[idx][1] = nums[start]
        return tree[idx]
    mid = (start + end) // 2
    now_left = init(start, mid, idx * 2)
    now_right = init(mid + 1, end, idx * 2 + 1)
    tree[idx][0] = min(now_left[0], now_right[0])
    tree[idx][1] = max(now_left[1], now_right[1])
    return tree[idx]

def get_m(start, end, idx, left, right) :
    if end < left or start > right :
        return [int(1e9), 0]
    if left <= start and end <= right :
        return tree[idx]
    mid = (start + end) // 2
    now_left = get_m(start, mid, idx * 2, left, right)
    now_right = get_m(mid + 1, end, idx * 2 + 1, left, right)
    return [min(now_left[0], now_right[0]),
            max(now_left[1], now_right[1])]

init(0, N - 1, 1)

# print(tree)

for i in range(M) :
    a, b = map(int, input().split())
    print(*get_m(0, N - 1, 1, a - 1, b - 1))