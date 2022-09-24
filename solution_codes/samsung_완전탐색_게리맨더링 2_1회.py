# 4:50 시작 1시간 30분 소요 .. 
# 선거구를 나누어서, max - min 의 최솟값을 구하자.
def div_reg(x, y, d1, d2, check_board):
    regs = {1:0, 2:0, 3:0, 4:0, 5:0}
    
    for r in range(n):
        for c in range(n):
            if check_board[r][c] != 5:
                if r < x+d1 and c <= y:
                    regs[1] += board[r][c]
                    check_board[r][c] = 1
                elif r <= x+d2 and y < c < n:
                    regs[2] += board[r][c]
                    check_board[r][c] = 2
                elif x+d1 <= r < n and c < y-d1+d2:
                    regs[3] += board[r][c]
                    check_board[r][c] = 3
                elif x+d2 < r < n and y-d1+d2 <= c < n:
                    regs[4] += board[r][c]
                    check_board[r][c] = 4
            else:
                regs[5] += board[r][c]
    for r in range(n):
        for c in range(n):
            if check_board[r][c] == 0:
                regs[5] += board[r][c]

                # check_board[r][c] = 5
    # print('check_board')
    # for c in check_board:
    #     print(c)
    return regs


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
min_val = int(1e9)

for x in range(n):
    for y in range(1, n-1):
         for d1 in range(1, y+1):
            for d2 in range(1, n-y):
                if d1 + d2 > n-(x+1):
                    continue
                else:       
                    # x, y, d1, d2 set
                    # print(x, y, d1, d2)
                    check_board = [[0]*n for _ in range(n)]
                    # 경계선 따라 5 채워넣기
                    for l1 in range(d1+1):
                        check_board[x+l1][y-l1] = 5
                        check_board[x+d2+l1][y+d2-l1] = 5
                    for l2 in range(d2+1):
                        check_board[x+l2][y+l2] = 5
                        check_board[x+d1+l2][y-d1+l2] = 5
                    # 경계선 만나면 안쪽에 5 채워넣기
                    dcount = 0
                    start = False
                    for cx in range(n):
                        row = check_board[cx][:]
                        if row.count(5) == 1:
                            continue
                        else:
                            on = False
                            for cy in range(n):
                                if not on and row[cy] == 5:
                                    on = True
                                    continue
                                elif on: check_board[cx][cy] = 5
                                if row[cy] == 5:
                                    break
       
                    regs = div_reg(x, y, d1 ,d2, check_board)
                    
                    regs_sort = sorted(regs.items(), key=lambda x: x[1])
                    # 차이 최댓값
                    dif = regs_sort[-1][1] - regs_sort[0][1]
                    # print('dif:', dif)
                    # 비교하여 갱신
                    if min_val > dif:
                        min_val = dif

print(min_val)