# 숫자를 입력 받아 오름차순
# 입력
"""
10 
1 4 3 2 5 9 8 6 7 10
"""


import sys
n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

# 버블정렬
print("---------버블정렬----------")

for i in range(len(num_list) - 1, 1, -1):
    for j in range(i):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

for i in num_list:
    print(i, end=" ")


# 선택정렬,
# 0~4, 1~4, 2~4
print()
print("---------선택정렬----------")

for i in range(len(num_list) - 1):
    min_index = i
    for j in range(i, len(num_list)):
        if num_list[j] < num_list[min_index]:
            min_index = j
    num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

for i in num_list:
    print(i, end=" ")


# 삽입정렬,
print()
print("---------삽입정렬----------")
for i in range(1, len(num_list)):
    print("i : ", end="")
    print(i)
    now_index = i
    while True:
        if num_list[now_index] < num_list[now_index - 1]:
            num_list[now_index], num_list[now_index -
                                          1] = num_list[now_index - 1], num_list[now_index]
            now_index -= 1
        else:
            break
    print("----------")

for i in num_list:
    print(i, end=" ")


# 퀵정렬
print()
print("---------퀵정렬----------")


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    low = start + 1
    high = end
    while low < high:
        while True:
            if low > end or array[low] > array[pivot]:
                break
            else:
                low += 1

        while True:
            if high < start + 1 or array[high] < array[pivot]:
                break
            else:
                high -= 1
        if low > high:
            array[high], array[pivot] = array[pivot], array[high]
            break
        else:
            array[high], array[low] = array[low], array[high]
    quick_sort(array, 0, high - 1)
    quick_sort(array, high + 1, end)


quick_sort(num_list, 0, len(num_list) - 1)

for i in num_list:
    print(i, end=" ")

# 병합정렬
print()
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
