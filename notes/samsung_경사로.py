# ~13:00
# n, l = map(int, input().split())
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))

n, l = 6, 2

# board = [ 
# [3, 3, 3, 3, 3, 3],
# [2, 3, 3, 3, 3, 3],
# [2, 2, 2, 3, 2, 3],
# [1, 1, 1, 2, 2, 2],
# [1, 1, 1, 3, 3, 1],
# [1, 1, 2, 3, 3, 2]]

board = [ 
[3, 2, 1, 1, 2, 3],
[3, 2, 2, 1, 2, 3],
[3, 2, 2, 2, 3, 3],
[3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 2, 2],
[3, 3, 3, 3, 2, 2],
]

# 회전 보드
rot_board = []
for i in range(n):
    rot_list = []
    for row in board:
        rot_list.append(row[i])
    rot_board.append(rot_list)


def cango(hor):
    visit = [False]*n # 경사로 놓은 위치 리스트
    for i in range(n-1):
        if abs(hor[i+1] - hor[i]) > 1:
            return False
        elif hor[i+1] == hor[i] + 1: # 다음칸이 한칸 더높은경우
            # 앞쪽에 L만큼 hor[i]와 같은 높이가 있는지 판단
            if i+1 >= l:
                if hor[i+1-l:i+1] == [hor[i] for _ in range(l)] and\
                    visit[i+1-l:i+1] == [False]*l: # 경사로 있는지도 판단
                    for v in range(i+1-l, i+1):
                        visit[v] = True 
                    # 존재하면 해당위치 경사로 세우기
                else: 
                    return False
            else: 
                return False

        elif hor[i+1] == hor[i] - 1: #한칸 더낮은경우
            # 다음 L만큼 hor[i+1]와 같은높이 있는지 판단
            if n-1-i >= l:
                if hor[i+1:i+1+l] == [hor[i+1] for _ in range(l)]:
                    for v in range(i+1, i+1+l):
                        visit[v] = True
                else: 
                    return False
            else: 
                return False
    print('passed!')
    print(hor, visit)
    return True

# 끝에서 끝까지 갈수있는지 판단
roads = 0
for hor in board:
    if cango(hor):
        roads += 1

for ver in rot_board:
    if cango(ver):
        roads += 1

print(roads)

    






    