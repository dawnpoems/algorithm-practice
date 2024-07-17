import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

nums = []

for i in range(N) :
    nums.append(int(input()))

tree = [0] * (N * 4)

def init(start, end, idx) :
    if start == end :
        tree[idx] = nums[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return tree[idx]

def get_sum(start, end, idx, left, right) :
    if end < left or start > right :
        return 0
    if left <= start and end <= right :
        print("sum : ", start, end, tree[idx])
        return tree[idx]
    mid = (start + end) // 2
    return get_sum(start, mid, idx * 2, left, right) + get_sum(mid + 1, end, idx * 2 + 1, left, right)

def update(start, end, idx, target, val) :
    if target < start or target > end :
        return
    print("update : ", start, end, idx, target, val)
    tree[idx] += val
    if start == end :
        return 
    mid = (start + end) // 2
    update(start, mid, idx * 2, target, val)
    update(mid + 1, end, idx * 2 + 1, target, val)

init(0, N - 1, 1)

print(tree)

for i in range(M + K) :
    a, b, c = map(int, input().split())
    if a == 1 :
        val = c - nums[b - 1]
        nums[b - 1] = c
        update(0, N - 1, 1, b - 1, val)
    else :
        print(get_sum(0, N - 1, 1, b - 1, c - 1))