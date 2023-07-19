import sys
from collections import Counter
input=sys.stdin.readline

n = int(input())

numbers = []
for i in range(n) :
    numbers.append(int(input()))

# print("-----")
# print(numbers)
print(round(sum(numbers) / n))
print(sorted(numbers)[n//2])
most_nums = sorted(Counter(numbers).most_common(), key=lambda x : (-x[1], x[0]))
# print(most_nums)
if len(most_nums) >= 2 and most_nums[0][1] == most_nums[1][1] :
    print(most_nums[1][0])
else :
    print(most_nums[0][0])
print(max(numbers) - min(numbers))