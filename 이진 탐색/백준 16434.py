import sys, math
input = sys.stdin.readline

N, H_atk = map(int, input().split())

rooms = []
for i in range(N) :
    rooms.append(list(map(int, input().split())))

def fight_monster(h_hp, h_atk, m_hp, m_atk) :
    lose_hp = (math.ceil(m_hp / h_atk) - 1) * m_atk
    return h_hp - lose_hp
    
def can_clear(h_max_hp) :
    global H_atk
    h_hp = h_max_hp
    h_atk = H_atk
    for room in rooms :
        t, a, h = room
        if t == 1 :
            h_hp = fight_monster(h_hp, h_atk, h, a)
            if h_hp <= 0 :
                return False
        if t == 2 :
            h_atk += a
            h_hp += h
            if h_hp > h_max_hp :
                h_hp = h_max_hp
    return True

start = 1
end = sys.maxsize
ans = end
while start <= end :
    mid = (start + end) // 2
    if can_clear(mid) :
        ans = mid
        end = mid - 1 
    else :
        start = mid + 1

print(ans)