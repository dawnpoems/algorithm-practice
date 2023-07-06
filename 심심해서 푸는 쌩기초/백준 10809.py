
alpha_list = [-1]*26

target_list = list(input())

for i in range(len(target_list)) :
    alpha_num = ord(target_list[i]) - 97
    if alpha_list[alpha_num] == -1 :
        alpha_list[alpha_num] = i

print(" ".join(list(map(str, alpha_list))))