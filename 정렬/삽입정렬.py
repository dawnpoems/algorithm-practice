# 숫자를 입력 받아 오름차순
# 입력
"""
10
1 4 3 2 5 9 8 6 7 10
"""

import sys
n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

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
