# 4:30 ~ 6:30
'''빙글빙글
구슬 1,2,3번. 연속하는 구슬 존재.
방향 di 와 거리 si를 정해서 해당 사정거리 내 구슬을 모두 없앤다.
구슬이동 : 번호 하나 작은칸이 빈칸이면, 빈칸으로 구슬 이동.
폭발하는 구슬 : 4개이상 연속한 구슬 - 없어짐.

폭발-이동-폭발-이동 계속반복.

폭발 안하면 - 구슬변화
구슬 변화 - 그룹 - A:개수 B:구슬번호 ex) 1 -> 1개, 1번 그러니까 1,1 로 변함. 한그룹당 2개.
칸수보다 많아지면 구슬은 없어진다.
'''
# n, m = map(int, input().split())

# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))

# magic = []
# for _ in range(m):
#     board.append(tuple(map(int, input().split())))

# 예제 1
# n, m = 7, 1

# board = [ 
# [0, 0, 0, 0, 0, 0, 0],
# [3, 2, 1, 3, 2, 3, 0],
# [2, 1, 2, 1, 2, 1, 0],
# [2, 1, 1, 0, 2, 1, 1],
# [3, 3, 2, 3, 2, 1, 2],
# [3, 3, 3, 1, 3, 3, 2],
# [2, 3, 2, 2, 3, 2, 3]
# ]

# magic = [(2,2)]


# 예제 2
# n, m = 7, 4
# board = [
# 0 0 0 2 3 2 3
# 1 2 3 1 2 3 1
# 2 3 1 2 3 1 2
# 1 2 3 0 2 3 1
# 2 3 1 2 3 1 2
# 3 1 2 3 1 2 3
# 1 2 3 1 2 3 1
# ]
# 1 3
# 2 2
# 3 1
# 4 3

# 1. 미로를 일렬로 펼치는 기능 구현

def stretch():
    st = []
    sx,sy = int((n+1)/2)-1, int((n+1)/2)-1 # 처음 상어 위치
    dx = (0,1,0,-1) # 좌하우상 순서로 돌아나감
    dy = (-1,0,1,0)
    path_len = 1
    dist = 0
    z = 0
    while True: # i는 8,24,48까지 도달 
        for _ in range(2): # 같은 길이로 두번씩 이동
            for i in range(path_len):
                sx += dx[z]
                sy += dy[z]
                dist += 1
                # print(dist)
                if dist == n*n:
                    return st
                # elif board[sx][sy] == 0:
                #     return
                st.append(board[sx][sy])
                # print(stretched)
            # 방향 바꿈
            z += 1
            if z == 4:
                z -= 4
        # 두번 가면 거리가 1 늘어남
        path_len += 1
    




# 2. 블리자드 마법 - 구슬 파괴
def bliz():
    bx = (-1,1,0,0)
    by = (0,0,-1,1)
    sx,sy = int((n+1)/2)-1, int((n+1)/2)-1 # 처음 상어 위치
    for di,si in magic: # (2,2) #di : 1234 상하좌우
        di -= 1 # 인덱스 맞춤
        for i in range(1,si+1): # 1~si 거리동안
            board[sx+i*bx[di]][sy+i*by[di]] = 0 # 파괴.
            

# for bo in board:
#     print(bo)
        

# 3. 모이고, 폭발을 반복하여 수행불가까지 실행 
## 폭발한 구슬 수 세어야함


def gather_and_explode():
    temp = [s for s in st]

    while True:
        # gather
        while 0 in temp:
            temp.remove(0)

        # explode
        ex_list = []  #[ [], [], []]
        ex_cand = []
        for j in range(len(temp)-1):
            if temp[j] == temp[j+1]:
                ex_cand.append(j)
                ex_cand.append(j+1)
            elif len(set(ex_cand)) >= 4:
                ex_list.append(list(set(ex_cand)))
                ex_cand = []
            else:
                ex_cand = []
        
        if not ex_list:
            return temp
        else:
            # 폭발 - 수 세어야함.
            for ex in ex_list:
                for e in ex:
                    marble[temp[e]] += 1
                    temp[e] = 0
            
# 4. 구슬 변화

def change_marble():
    # for m in st:
    temp = []
    same_count = 1
    for j in range(len(st)-1):
        if st[j] == st[j+1]:
            same_count += 1 
            if j == len(st)-2:
                temp.append(same_count)
                temp.append(st[j])
                break
        else:
            temp.append(same_count)
            temp.append(st[j])
            same_count = 1
            if j == len(st)-2:
                temp.append(same_count)
                temp.append(st[j+1])
                break

    # 칸수보다 크면 잘라내기
    return temp[:n*n]

## 5. 마지막. 다시 결과를 칸에 넣기
def fold(input_list):
    stret = [i for i in input_list]
    empty_board = [[0]*n for _ in range(n)]
    sx,sy = int((n+1)/2)-1, int((n+1)/2)-1 # 처음 상어 위치
    dx = (0,1,0,-1) # 좌하우상 순서로 돌아나감
    dy = (-1,0,1,0)
    path_len = 1
    dist = 0
    z = 0
    while True: # i는 8,24,48까지 도달 
        for _ in range(2): # 같은 길이로 두번씩 이동
            for i in range(path_len):
                sx += dx[z]
                sy += dy[z]
                dist += 1
                # print(dist)
                if dist == n*n or len(stret) == 0:
                    return empty_board
                empty_board[sx][sy] = stret.pop(0)
                # print(stretched)
            # 방향 바꿈
            z += 1
            if z == 4:
                z -= 4
        # 두번 가면 거리가 1 늘어남
        path_len += 1


marble = {1:0, 2:0, 3:0}
for _ in range(m):
    bliz()
    st = stretch()

    

    st = gather_and_explode()

    marb_changed = change_marble()
    # print('marb change')
    # print(marb_changed)

    result = fold(marb_changed)
    # print('result:')
    # for res in result:
    #     print(res)
        
    board = [b[:] for b in result]


answer = 0
for m in marble:
    answer += marble[m]*m
print(answer)


            