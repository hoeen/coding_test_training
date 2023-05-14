import sys
sys.setrecursionlimit(int(1e5))

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
board = [[[float('inf')] * 3 for _ in range(3)] for _ in range(n)]

# top-down dp
def recur(idx, color, first_color):
    if idx == n: # 맨끝 - 0으로 리턴
        return 0
    if board[idx][color] < float('inf'):
        return board[idx][color]
    for next_col in range(3):
        if idx == n-2 and next_col in [first_color, color]:
            continue
        elif next_col != color:
            board[idx][color] = min(board[idx][color], 
                                costs[idx][color] + recur(idx+1, next_col, first_color)
                                )
    return board[idx][color]

min_cost = float('inf')
for i in range(3):
    # first_color의 경우마다 dp table를 새로 만들어줘서 재귀 결과를 최솟값과 비교 갱신
    board = [[float('inf')] * 3 for _ in range(n)]
    min_cost = min(min_cost, 
                    recur(0, i, i)
                    )
print(min_cost)
