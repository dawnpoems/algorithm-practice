import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))


def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)


array.sort()

for target in targets:
    print(binary_search(array, target, 0, n-1))
