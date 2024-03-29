import sys
input = sys.stdin.readline

N, C = map(int, input().split())

weis = list(map(int, input().split()))

a_weis = weis[:N // 2]
b_weis = weis[N // 2:]

a_sums = []
b_sums = []

def brut(total, depth, wei_lst, sum_lst) :
    if depth >= len(wei_lst) :
        sum_lst.append(total)
        return
    brut(total, depth + 1, wei_lst, sum_lst)
    brut(total + wei_lst[depth], depth + 1, wei_lst, sum_lst)

def bi_search(start, end, target, lst) :
    while start < end :
        mid = (start + end) // 2
        if lst[mid] <= target :
            start = mid + 1
        else :
            end = mid
    return end

brut(0, 0, a_weis, a_sums)
brut(0, 0, b_weis, b_sums)

b_sums.sort()
cnt = 0
for a in a_sums :
    if C - a < 0 :
        continue
    cnt += bi_search(0, len(b_sums), C - a, b_sums)

print(cnt)