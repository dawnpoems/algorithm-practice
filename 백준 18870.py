import sys
n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))


answer = [0] * n


num_with_index = []
for i in range(len(num_list)):
    num_with_index.append([i, num_list[i]])

num_with_index.sort(key=lambda x: x[1])

comp_num = 0
tmp_num = num_with_index.pop(0)[1]

for i in num_with_index:
    if i[1] == tmp_num:
        answer[i[0]] = comp_num
    else:
        tmp_num = i[1]
        comp_num += 1
        answer[i[0]] = comp_num

print(" ".join(list(map(str, answer))))
