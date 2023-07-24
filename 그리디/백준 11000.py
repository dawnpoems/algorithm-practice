import sys
input = sys.stdin.readline

n = int(input())

times = []

for i in range(n) :
    times.append(list(map(int, input().strip().split())))

times.sort(key=lambda x : (x[1], x[0]))

spaces = []

def find_posi (array ,target):
        start = 0
        end = len(array) - 1
        while start <= end :
            # print(start, end=":")
            # print(end)
            mid = (start + end) // 2
            if array[mid] == target :
                result = mid
                break
            elif array[mid] < target :
                result = mid
                start = mid + 1
            else :
                end = mid - 1
        return result


for i, time in enumerate(times) :
    # print("-----")
    if len(spaces) <= 0 :
        spaces.append(time[1])
    else :
        if spaces[0] > time[0] : #가장 일찍 끝나는 시간이 이번꺼 시작시간보다 느리면
            posi = find_posi(spaces, time[1])
            # print("11111")
            # print(posi)
            spaces.insert(posi + 1, time[1])
        else : #원래 강의실에서 시작 가능.
            p = find_posi(spaces, time[0])
            # print("22222")
            # print(p)

            posi = find_posi(spaces, time[1])
            del spaces[p]
            spaces.insert(posi, time[1])
            # print("33333")
            # print(posi)

    # print("------")
    # print(time)
    # print(spaces)

print(len(spaces))