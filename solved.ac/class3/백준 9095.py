import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

def find_dp(num) :
    if dp[num] != 0 :
        return dp[num]
    dp[num] = find_dp(num - 1) + find_dp(num - 2) + find_dp(num - 3)
    return dp[num]
        
for i in range(n) :
    now = int(input())
    print(find_dp(now))
    
    
    
