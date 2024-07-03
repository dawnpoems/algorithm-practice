import sys
input = sys.stdin.readline

N, M = map(int, input().split())

titles = []
powers = []
for i in range(N) :
    title, power_str = input().split()
    power = int(power_str)
    if len(powers) == 0 or powers[-1] != power :
        titles.append(title)
        powers.append(power)

def bi_search(target) :
    start = 0
    end = len(powers)
    while start < end :
        mid = (start + end) // 2
        if powers[mid] < target :
            start = mid + 1
        elif powers[mid] >= target :
            end = mid
    return end

for i in range(M) :
    char = int(input())
    idx = bi_search(char)
    print(titles[idx])