import sys
input = sys.stdin.readline

n = int(input())

max_a = max_b = max_c = min_a= min_b = min_c = 0
for i in range(n) :
    a, b, c = map(int, input().split())
    n_max1 = max(max_a, max_b) + a
    n_max2 = max(max_a, max_b, max_c) + b
    n_max3 = max(max_b, max_c) + c

    n_min1 = min(min_a, min_b) + a 
    n_min2 = min(min_a, min_b, min_c) + b
    n_min3 = min(min_b, min_c) + c

    max_a = n_max1
    max_b = n_max2
    max_c = n_max3
    min_a = n_min1
    min_b = n_min2
    min_c = n_min3

    # print("--------")
    # print(max_a, max_b, max_c)
    # print(min_a, min_b, min_c)
print(max(max_a, max_b, max_c), min(min_a, min_b, min_c))