# ~4:00 까지 해결. 1시간 20분  - 디버깅 15분 더 ... 
# ~4:57 에 결국 해결. 총 소요시간 2시간 10분.. 

from itertools import combinations
''' 
궁수 3명이 동시에 공격
거리가 D이하인 적 중에 가장 가까운 적. 여럿일 경우 가장 왼쪽부터 공격 (격자 거리)
공격 후 적은 아래로 한칸 이동. 성으로 이동하면 제외됨. 
적이 모두 제외되면 게임 끝.
궁수의 공격으로 제거할 수 있는 적의 최대수 계산
'''

n, m, d = map(int, input().split())

# n, m, d = 6, 5, 1

board = [list(map(int, input().split())) for _ in range(n)]

# board = [ 
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0],

# ]

# board = [ 
# [1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1],
# ]

# board = [ 
# [1, 0, 1, 0, 1],
# [0, 1, 0, 1, 0],
# [1, 1, 0, 0, 0],
# [0, 0, 0, 1, 1],
# [1, 1, 0, 1, 1],
# [0, 0, 1, 0, 0],
# ]


org_board = [b[:] for b in board]


# d만큼 탐색 구현
def find_enemy(ay):
    # 왼쪽부터 탐색
    # breakpoint()
    for dist in range(1, d+1): # 1~d 
        for y in range(-dist, dist+1):
            for x in range(1, dist-abs(y)+1): # 합 d 이하의 x, y
                if 0 <= n-x and 0 <= ay+y < m:
                    if board[n-x][ay+y] == 1:
                        return n-x, ay+y

    # # 못찾으면, 오른쪽 탐색
    # for y in range(1, d):
    #     for x in range(1, d-abs(y)+1): # 합 d 이하의 x, y
    #         if 0 <= n-x and 0 <= ay+y < m:
    #             if board[n-x][ay+y] == 1:
    #                 return n-x, ay+y
    
    return None, None

# 적 제거 구현
def kill_enemy(ex, ey):
    global count
    if board[ex][ey] == 1:
        count += 1
        board[ex][ey] = 0
    return

def push():
    global board
    new_board = [[] for _ in range(n)]
    new_board[0] = [0]*m
    for row in range(n-1):
        new_board[row+1] = board[row][:]
    # 기존 board를 대체
    board = [b[:] for b in new_board]
    return


# 궁수의 위치 선정 구현
def arch_pos():
    # m 열 중 3개 뽑기 
    return list(combinations(range(0,m), 3))
    
# print(arch_pos())

pos_list = arch_pos()
max_count = 0
for archs in pos_list:
    count = 0
    board = [b[:] for b in org_board]

    # print('check')
    # print(archs)

    while sum([sum(b) for b in board]) != 0:
        
        # print('board')
        # for b in board:
        #     print(b)

        enemy_pos = set()
        for ai in archs: #a1, a2, a3
            enemy_pos.add(find_enemy(ai))
        # enemy_pos = list(enemy_pos)
        # enemy_pos.sort(key=lambda x: (x[1], -x[0])) # 왼쪽부터, 아래부터 정렬
        for ex, ey in enemy_pos:
            # print('enemy pos:', (ex, ey))
            if (ex, ey) != (None, None):
                kill_enemy(ex, ey)
        push()

    # print('total killed:', count)
    if max_count < count:
        max_count = count

print(max_count)