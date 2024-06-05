import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().strip().split()))
numbers.insert(0, 0)

d = [0]
a = [0]

def bi_find(x) :
    start = 0
    end = len(a) - 1
    result = end
    while start <= end :
        mid = (start + end) // 2
        if a[mid] == x :
            result = mid
            break
        elif a[mid] > x :
            result = mid
            end = mid -1
        else :
            start = mid + 1
    return result

for i in range(1, len(numbers)) :
    if numbers[i] > a[-1] :
        d.append(d[-1] + 1)
        a.append(numbers[i])
    else :
        #위치 찾아서 a 갱신하기.
        p = bi_find(numbers[i])
        a[p] = numbers[i]
    
    # print("------")
    # print(numbers[i])
    # print(d)
    # print(a)

print(d[-1])
