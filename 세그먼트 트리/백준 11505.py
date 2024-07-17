import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

nums = []

for i in range(N) :
    nums.append(int(input()))

tree = [0] * (N * 4)

MOD = 1000000007

def init(start, end, idx) :
    if start == end :
        tree[idx] = nums[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = (init(start, mid, idx * 2) * init(mid + 1, end, idx * 2 + 1)) % MOD
    return tree[idx]

def get_multi(start, end, idx, left, right) :
    if end < left or start > right :
        return 1
    if left <= start and end <= right :
        # print("multi : ", start, end, tree[idx])
        return tree[idx]
    mid = (start + end) // 2
    return (get_multi(start, mid, idx * 2, left, right) * get_multi(mid + 1, end, idx * 2 + 1, left, right)) % MOD

def update(start, end, idx, target, val) :
    if target < start or target > end :
        return tree[idx]
    if start == end :
        tree[idx] = val
        # print("update : ", start, end, target, val, tree[idx])
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = (update(start, mid, idx * 2, target, val) * update(mid + 1, end, idx * 2 + 1, target, val)) % MOD
    # print("update : ", start, end, target, val, tree[idx])
    return tree[idx]

init(0, N - 1, 1)

# print(tree)

for i in range(M + K) :
    a, b, c = map(int, input().split())
    if a == 1 :
        update(0, N - 1, 1, b - 1, c)
        nums[b - 1] = c
    else :
        print(get_multi(0, N - 1, 1, b - 1, c - 1))