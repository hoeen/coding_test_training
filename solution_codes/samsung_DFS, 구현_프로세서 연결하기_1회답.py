# ~6:00
# n = 7
# board = [ 
# [0, 0, 1, 0, 0, 0, 0],
# [0, 0, 1, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 1, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [1, 1, 0, 1, 0, 0, 0],
# [0, 1, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# ]

n = 11 
board = [ 
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
[0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# 가장자리까지 전선 뻗어서 최대한 연결. 전선 길이의 최솟값 
dx = (-1, 1, 0, 0) # 상하좌우
dy = (0, 0, -1, 1)

def core_pos(board):
    pos_list = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                pos_list.append((x,y))
    return pos_list

# 1 core   /  -1 wire
def dfs(pos_idx, board, cores, wires):
    
    if pos_idx == len(pos_list):
        core_wire.append((cores, wires))
        return 

    x, y = pos_list[pos_idx]
    for i in range(4):  
        if i == 0:  # 상
            view = [b[y] for b in board[:x]]
        elif i == 1: # 하 
            view = [b[y] for b in board[x+1:]]
        elif i == 2: # 좌
            view = board[x][:y]
        else: #i == 3 # 우
            view = board[x][y+1:]

        # print('view:', view)

        new_board = [b[:] for b in board]

        if len(view) == 0:     # 붙어있음 - 연결된걸로 간주
            new_cores = cores + 1   
            new_wires = wires
            
        elif 1 not in view and -1 not in view: # 비어있음 - 채우기
            new_cores = cores + 1   
            new_wires = wires + len(view)
            
            # 채우기
            if i == 0:  # 상
                for b in new_board[:x]:
                    b[y] = -1
            elif i == 1: # 하 
                for b in new_board[x+1:]:
                    b[y] = -1
            elif i == 2: # 좌
                for iy in range(0, y):
                    new_board[x][iy] = -1 
            else: #i == 3 # 우
                for iy in range(y+1, n):
                    new_board[x][iy] = -1 

        else: # 안비어있음 - 넘어감
            new_cores = cores
            new_wires = wires
            
        dfs(pos_idx+1, new_board, new_cores, new_wires)
        
        
        
    
 
core_wire = []



pos_list = core_pos(board)
dfs(0, board, 0, 0)

core_wire.sort(key=lambda x: (-x[0], x[1]))

# print(core_wire)
# print(len(core_wire))
print(core_wire[0][1])

# print(pos_list)
    



