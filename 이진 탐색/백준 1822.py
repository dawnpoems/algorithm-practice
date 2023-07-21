import sys
input = sys.stdin.readline

na, nb = map(int, input().strip().split())

a_list = list(map(int, input().strip().split()))

b_list = list(map(int, input().strip().split()))

b_list.sort()

cnt = 0
answers = []

for a in a_list :
    start = 0
    end = nb - 1
    have_flag = False

    while start <= end :
        mid = (start + end) // 2
        now = b_list[mid]
        if now == a :
            have_flag = True
            break
        elif now < a :
            start = mid + 1
        else :
            end = mid - 1

    if not have_flag :
        cnt += 1
        answers.append(a)

answers.sort()
print(cnt)
if cnt > 0 :
    print(" ".join(map(str, answers)))