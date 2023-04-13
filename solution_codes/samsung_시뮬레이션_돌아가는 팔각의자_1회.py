## 주석처리 해지하면 input.txt에서 입력을 읽어올 수 있음
# import sys
# sys.stdin = open('input.txt', 'r')

board = [list(map(int, input())) for _ in range(4)]
n = int(input())

def rotate(num, di):
    if di == 1: # 시계 - 마지막이 앞에옴
        board[num-1] = [board[num-1][-1]] + board[num-1][:-1] 
    elif di == -1:
        board[num-1] = board[num-1][1:] + [board[num-1][0]]

def check(num, di): # 다른의자 회전할지 말지 판단 - 의자 기준으로 왼쪽, 오른쪽 끝까지
    rot_list = [0]*4
    rot_list[num-1] = di

    left, right = board[num-1][6], board[num-1][2]
    cur_di = di
    # 왼쪽
    for i in range(num-2, -1, -1):
        next_left, next_right = board[i][6], board[i][2]
        if next_right == left:
            break # 회전 안하므로 멈춤
        else:
            cur_di *= -1 # 반대방향
            rot_list[i] = cur_di 
            left = next_left 

    cur_di = di
    # 오른쪽
    for j in range(num, 4):
        next_left, next_right = board[j][6], board[j][2]
        if next_left == right:
            break 
        else:
            cur_di *= -1
            rot_list[j] = cur_di
            right = next_right

    return rot_list

for _ in range(n):
    table, direc = map(int, input().split())
    rotate_list = check(table, direc) # [-1, 1, -1, 1]
    
    for k in range(1, 5):
        rotate(k, rotate_list[k-1])

ans = []
for i in range(4):
    ans.append(board[i][0])

print(1*ans[0] + 2*ans[1] + 4*ans[2] + 8*ans[3])