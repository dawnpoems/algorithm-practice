import sys

input = sys.stdin.readline

n = int(input())

count = n

for i in range(n) :
    spells = list(input())
    checked_list = []
    for spell in spells :
        if spell in checked_list and spell != checked_list[-1] :
            count -= 1
            break
        else :
            checked_list.append(spell)

print(count)


    


