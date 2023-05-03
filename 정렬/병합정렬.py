# 숫자를 입력 받아 오름차순
# 입력
"""
10 
1 4 3 2 5 9 8 6 7 10
"""

import sys
n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

# 병합정렬
print("---------병합정렬----------")


def merge_sort(array):
    if len(array) <= 1:
        return array

    left = array[:len(array)//2]
    right = array[len(array)//2:]
    left_array = merge_sort(left)
    right_array = merge_sort(right)
    return merge(left_array, right_array)


def merge(left, right):
    merged_list = []
    i = 0
    j = 0
    while True:
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
        if i >= len(left) or j >= len(right):
            break

    while i < len(left):
        merged_list.append(left[i])
        i += 1
    while j < len(right):
        merged_list.append(right[j])
        j += 1

    return merged_list


for i in merge_sort(num_list):
    print(i, end=" ")
