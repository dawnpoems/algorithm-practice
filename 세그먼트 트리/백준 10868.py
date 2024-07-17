import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []

for i in range(N) :
    nums.append(int(input()))

tree = [0] * (N * 4)

def init(start, end, idx) :
    if start == end :
        tree[idx] = nums[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = min(init(start, mid, idx * 2), init(mid + 1, end, idx * 2 + 1))
    return tree[idx]

def get_min(start, end, idx, left, right) :
    if end < left or start > right :
        return int(1e9)
    if left <= start and end <= right :
        # print("min : ", start, end, tree[idx])
        return tree[idx]
    mid = (start + end) // 2
    return min(get_min(start, mid, idx * 2, left, right), get_min(mid + 1, end, idx * 2 + 1, left, right))

init(0, N - 1, 1)

# print(tree)

for i in range(M) :
    a, b = map(int, input().split())
    print(get_min(0, N - 1, 1, a - 1, b - 1))