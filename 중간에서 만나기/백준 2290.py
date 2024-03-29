import sys
input = sys.stdin.readline

N = int(input())
nums = []
for i in range(N) :
    nums.append(int(input()))

nums.sort(reverse=True)
total_plus = set()

for i in nums :
    for j in nums :
        total_plus.add(i + j)

totals = sorted(list(total_plus))

def bi_search(target, lst) :
    start = 0
    end = len(lst) - 1
    while start <= end :
        mid = (start + end) // 2
        if lst[mid] == target :
            return mid
        elif lst[mid] < target :
            start = mid + 1
        else :
            end = mid - 1
    return -1

def find_max(nums, totals) : 
    for i in nums :
        for j in nums :
            if i - j > 0 :
                ret = bi_search(i - j, totals)
                if ret > -1 :
                    return i

print(find_max(nums, totals))