# ~9:00
# 색종이 5종류를 5개씩 가지고 있음.
# 큰것부터 채울수 있는 경우를 찾는다.
# 색종이는 dict로 해서 쓸때마다 뺌.
# 
import time
board = [
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# board = [
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
# [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
# [0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
# ]

board = [
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
[1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
[0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

board = [ 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# board = [list(map(int, input().split())) for _ in range(10)]
def fill(board, size, count):
    # index = 4 # 제일 큰것부터 시작
    # while index >= 0:
    #     if cp[index] > 0:
    #         cp[index] -= 1 # 색종이 하나 쓰기   
    #     else:
    #         index -= 1
    #         continue # 더 작은종이로
        # breakpoint()
    new_board = [b[:] for b in board]
    for x in range(0, 10-(size-1)):
        for y in range(0, 10-(size-1)):
            view = [b[y:y+size] for b in board[x:x+size]]
            # 모두 1로 채워진 경우 - 0으로 로 채우고 리턴
            if sum([sum(v) for v in view]) == size**2:
                # 0으로 채움
                for cx in range(x, x+size):
                    for cy in range(y, y+size):
                        new_board[cx][cy] = 0
                return new_board, count+1
    # 맞는 부분이 없을 경우 리턴
    return new_board, count 
        

def dfs(board, cp, count):
    # 완전탐색 - 그리디로 접근하지말고 모든 경우에서 따져야함.
    # 한 함수당 모든 색종이 종류로 재귀 들어가자.
    global min_count

    # time.sleep(0.5)
    print('check')
    for b in board:
        print(b)
    print(cp)
    print(count)

    if sum(cp[1:]) == 0 and sum([sum(b) for b in board]) > cp[0]: # 1개짜리로 남은칸 다 못덮으면 
        return
    elif sum([sum(b) for b in board]) == 0: 
        # 색종이 남고 모든 칸이 0이면 - 다 덮었으므로 색종이 개수 갱신
        if count < min_count or min_count == -1:
            min_count = count
        return
    else:
        for size in range(5,0,-1):
            if cp[size-1] > 0: # 사이즈의 종이 남은경우
                new_board, new_count = fill(board, size, count)
                new_cp = [c for c in cp]
                if new_count == count: # 종이 못쓴경우 : 해당 종이 수를 0으로 만들고 재귀.
                    new_cp[size-1] = 0
                    dfs(new_board, new_cp, new_count)
                else:
                    new_cp[size-1] -= 1 # 해당 사이즈 종이 사용하고 재귀
                    dfs(new_board, new_cp, new_count)
                    
                
                
    
        

min_count = -1
dfs(board, [5,5,5,5,5], 0)
# fill(board, [5,5,5,5,5], 0)
print(min_count)

