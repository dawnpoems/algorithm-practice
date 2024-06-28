import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

# m보다 작거나 같은 숫자의 갯수가 K개 보다 많아야 한다!
# 에 해당하는 m의 최을 이분탐색으로 찾아보겠습니다.

#나머지를 버린 값을 다 더하기.
# 한 행에서 m 보다 작거나 같은 숫자의 갯수는 m/i(행 숫자)네..
#i행의 숫자들은 i*1, i*2, i*3, ..., i*N으로 구성되어 있다.
#i행의 숫자들 중 m보다 작거나 같은 숫자는 (i*j <= m)를 만족하는 j의 개수이고
#이는 i*1, i*2, ..., i*j이므로, m/i와 같은 값이 된다.

def get_smaller_cnt(m) :
    ans = 0
    for i in range(1, N + 1) :
        ans += min(m // i, N)
    # print(ans)
    return ans

def bi_search(start, end, target) :
    while start <= end :
        mid = (start + end) // 2
        # print(start, end, mid)
        if get_smaller_cnt(mid) < target :
            start = mid + 1
        else :
            ret = mid
            end = mid - 1
    return ret
    
print(bi_search(1, K, K))