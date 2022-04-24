# ~3:30 / 4:00
n = int(input())

board0 = []
for _ in range(n):
    board0.append(list(map(int, input().split())))

# board0 = [ 
#     [2,4,16,8],
#     [8,4,0,0],
#     [16,8,2,0],
#     [2,8,2,0]
# ]

'''
최대 5번 이동해서 만들 수 있는 가장 큰 블록값 구하기
초기상태에서 합만 제대로 수행하면됨
'''
# 위치 찾기
def find():
    crd = []
    for x in range(n):
        for y in range(n):
            if board[x][y] != 0:
                crd.append((x,y))
    return crd


# 1. 이동 구현
dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]
def move(dir):
    num_list = {}
    coor = sorted(find())
    if dir == 1:
        coor = sorted(sorted(coor), key = lambda x: x[1])
        
        for co in coor:
            # board 값 집어넣기
            val = board[co[0]][co[1]]
            # board 0 초기화
            board[co[0]][co[1]] = 0

            # 민 좌표 생성. 밀고 합치기!
            xc = 0
            while (xc, co[1]) in num_list:
                xc += 1
            # 이전 좌표값이 같은지 확인
            if xc == 0:
                switch = 0
            # 이전 좌표값이 같은지 확인
            if xc > 0 and num_list[(xc-1,co[1])] == val and switch == 0:
                num_list[(xc-1,co[1])]+=val # 이전값을 곱해줌
                # 지금좌표는 추가하지 않음
                switch = 1
            else:
                num_list[(xc,co[1])] = val
                # push_list.append((xc, co[1]))
                switch = 0



    elif dir == 2:
        coor = sorted(sorted(coor, reverse=True), key = lambda x: x[1])
        for co in coor:
            # board 값 집어넣기
            val = board[co[0]][co[1]]
            # board 0 초기화
            board[co[0]][co[1]] = 0

            # 민 좌표 생성. 밀고 합치기!
            xc = n-1
            while (xc, co[1]) in num_list:
                xc -= 1
            
            if xc == n-1:
                switch = 0
            # 이전 좌표값이 같은지 확인
            if xc < n-1 and num_list[(xc+1,co[1])] == val and switch == 0:
                num_list[(xc+1,co[1])]+=val # 이전값을 곱해줌
                # 지금좌표는 추가하지 않음
                switch = 1
            else:
                num_list[(xc,co[1])] = val
                switch = 0
                
    elif dir == 3:
        coor = sorted(sorted(coor), key = lambda x: x[0])
        for co in coor:
            # board 값 집어넣기
            val = board[co[0]][co[1]]
            # board 0 초기화
            board[co[0]][co[1]] = 0

            # 민 좌표 생성. 밀고 합치기!
            xc = 0
            while (co[0],xc) in num_list:
                xc += 1
            # 이전 좌표값이 같은지 확인
            if xc == 0:
                switch = 0
            # 이전 좌표값이 같은지 확인
            if xc > 0 and num_list[(co[0],xc-1)] == val and switch == 0:
                num_list[(co[0],xc-1)]+=val # 이전값을 곱해줌
                switch = 1
                # 지금좌표는 추가하지 않음
            else:
                num_list[(co[0],xc)] = val
                switch = 0
                
    else: # 4
        coor = sorted(sorted(coor, reverse=True), key = lambda x: x[0])
        for co in coor:
            # board 값 집어넣기
            val = board[co[0]][co[1]]
            # board 0 초기화
            board[co[0]][co[1]] = 0

            # 민 좌표 생성. 밀고 합치기!
            xc = n-1
            while (co[0],xc) in num_list:
                xc -= 1

            
            # 이전 좌표값이 같은지 확인
            if xc == n-1:
                switch = 0
            if xc < n-1 and num_list[(co[0],xc+1)] == val and switch == 0:
                num_list[(co[0],xc+1)]+=val # 이전값을 곱해줌
                # 이전값 바뀌었을때, 스위치 켠다
                switch = 1
                # 지금좌표는 추가하지 않음
            else:
                num_list[(co[0],xc)] = val
                switch = 0
               
    
    # 옮긴 값 채워넣기
    for key in num_list:
        board[key[0]][key[1]] = num_list[key]
        
# board = [item[:] for item in board0]
# for i in [1]:
#     move(i)
#     for bo in board:
#         print(bo)
#     print('='*30)

max_cand = []

for i1 in range(1,5):
    for i2 in range(1,5):
        for i3 in range(1,5):
            for i4 in range(1,5):
                for i5 in range(1,5):
                    
                    board = [item[:] for item in board0]


                    cand = [i1,i2,i3,i4,i5]
                    for ca in cand:
                        move(ca)
                        
                    bef = 0
                    for row in range(n):
                        for col in range(n):
                            val = board[row][col]
                            if bef < val:
                                bef = val

                    
                    max_cand.append(bef)

print(max(max_cand))
