import sys
input = sys.stdin.readline

lst = list(input().strip())

start = 0
end = len(lst) - 1

plus = 0
while start < end :
    # print(start, end)
    while end < len(lst) and lst[start] != lst[end]:
        plus += 1
        end += 1
    start += 1
    end -= 1

# print(plus)
print(len(lst) + plus)