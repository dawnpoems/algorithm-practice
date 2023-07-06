import sys

input = sys.stdin.readline

start = input()
        
tag_flag = False
answer_list = []
now_list = []
for word in list(start) :
    if word == "<" :
        if len(now_list) > 0 :
            if tag_flag == False :
                now_list.reverse()
            answer_list.append("".join(now_list))
            now_list = []
        tag_flag = True
    
    if tag_flag :
        now_list.append(word)
    else :
        if word == " " :
            now_list.reverse()
            answer_list.append("".join(now_list))
            answer_list.append(word)
            now_list = []
        else :
            now_list.append(word)

    if word == ">" :
        answer_list.append("".join(now_list))
        now_list = []
        tag_flag = False

if tag_flag == False :
    now_list.reverse()

answer_list.append("".join(now_list).strip())

print("".join(answer_list))
