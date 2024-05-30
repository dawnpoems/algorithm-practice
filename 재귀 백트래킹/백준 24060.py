import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

ans_lst = []
def merge(nums, start, mid, end) :
    i = start
    j = mid + 1
    tmp = []
    while i <= mid and j <= end :
        if nums[i] <= nums[j] :
            tmp.append(nums[i])
            i += 1
        else :
            tmp.append(nums[j])
            j += 1
    while i <= mid :
        tmp.append(nums[i])
        i += 1
    while j <= end :
        tmp.append(nums[j])
        j += 1
    for i in range(end - start + 1) :
        nums[start + i] = tmp[i]
        ans_lst.append(tmp[i])
        
def merge_sort(nums, start, end) :
    if start < end :
        mid = (start + end) // 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid + 1, end)
        merge(nums, start, mid, end)

merge_sort(nums, 0, N - 1)

if len(ans_lst) >= K :
    print(ans_lst[K - 1])
else :
    print(-1)