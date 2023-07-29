import sys
input = sys.stdin.readline

n = int(input())

lines = []
for i in range(n) :
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort()

numbers = [0]
for line in lines :
    numbers.append(line[1])

# print(numbers)

d = [0]
a = [0]

def find_min_a(num) :
    start = 0
    end = len(a) - 1
    result = end
    while start <= end :
        mid = (start + end) // 2
        if a[mid] == num :
            result = mid
            break
        elif a[mid] > num :
            result = mid
            end = mid - 1
        else :
            start = mid + 1
    return result

for i in range(1, len(numbers)) :
    if numbers[i] > a[-1] :
        d.append(d[-1] + 1)
        a.append(numbers[i])
    else :
        p = find_min_a(numbers[i])
        a[p] = numbers[i]
    # print("---------")
    # print("d = ", end="")
    # print(d)
    # print("a = ", end="")
    # print(a)
print(n - d[-1])

