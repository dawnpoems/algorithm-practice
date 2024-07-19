import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

tree = [0] * (N * 4)

def get_sum(start, end, idx, left, right) :
    if end < left or start > right :
        return 0
    if left <= start and end <= right :
        return tree[idx]
    mid = (start + end) // 2
    return get_sum(start, mid, idx * 2, left, right) + get_sum(mid + 1, end, idx * 2 + 1, left, right)

def update(start, end, idx, target, val) :
    if target < start or target > end :
        return
    tree[idx] += val
    if start == end :
        return
    mid = (start + end) // 2
    update(start, mid, idx * 2, target, val)
    update(mid + 1, end, idx * 2 + 1, target, val)

for i in range(Q) :
    c, p, x = map(int, input().split())
    if c == 1 :
        update(0, N - 1, 1, p - 1, x)
    elif c == 2 :
        print(get_sum(0, N - 1, 1, p - 1, x - 1))

