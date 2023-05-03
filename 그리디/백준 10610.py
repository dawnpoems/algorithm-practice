import sys

my_list = list(sys.stdin.readline().rstrip())
my_list.sort(reverse=True)

if my_list.pop() != "0":
    print(-1)

else:
    sum = 0
    answer = ""
    for num in my_list:
        sum += int(num)
        answer += num
    if sum % 3 == 0:
        print(int(answer)*10)
    else:
        print(-1)
