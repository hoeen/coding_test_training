# 9:10 ~ 

def rotate(xi, di, ki):
    global board
    mul = xi
    # print('rotate:', xi, di, ki)
    while xi <= n:
        if di == 0: # 시계 방향, 1이면 반시계
            board[xi-1] = board[xi-1][:][-ki:] + board[xi-1][:][:-ki]
        else:
            board[xi-1] = board[xi-1][:][ki:] + board[xi-1][:][:ki]
        xi += mul
    #     print('xi:', xi)
    # for b in board:
    #     print(b)



def find_near():
    # 인접 - 같은 행에서 앞뒤 / 같은 열에서 앞뒤
    new_board = [b[:] for b in board]
    near = False
    for plt in range(n):
        for num in range(m):
            if plt == 0:
                pdl = [(plt+1) % n]
            elif plt == n-1:
                pdl = [(plt-1) % n]
            else:
                pdl = [(plt-1) % n, (plt+1) % n]
            if board[plt][num]:
                for pd in pdl:
                    if board[pd][num] == board[plt][num]:
                        # print('pd, plt, num:', pd, plt, num)
                        near = True
                        new_board[plt][num] = 0
                        new_board[pd][num] = 0
                for d in (-1, 1):
                    nd = (num+d) % m
                    if board[plt][nd] == board[plt][num]:
                        # print('pd, plt, num:', pd, plt, num)
                        near = True
                        new_board[plt][num] = 0
                        new_board[plt][nd] = 0
    if not near:
        # print('not near')
        num_count = 0
        num_sum = 0
        for plt in range(n):
            for num in range(m):
                if new_board[plt][num] > 0:
                    num_count += 1
                    num_sum += new_board[plt][num]
        if num_count != 0:
            num_mean = num_sum / num_count
        else:
            num_mean = 0
        # print('mean:', num_mean)
        for plt in range(n):
            for num in range(m):
                if new_board[plt][num] > 0:
                    if new_board[plt][num] < num_mean:
                        new_board[plt][num] += 1
                    elif new_board[plt][num] > num_mean:
                        new_board[plt][num] -= 1
    
    # print('near:')
    # for b in new_board:
    #     print(b)
    
    return new_board


n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
coms = [tuple(map(int, input().split())) for _ in range(t)]
# xi의 배수인 원판을   di 방향으로 0 시계 1 반시계  ki 회전

# 1. com따라 회전시킴
for xi, di, ki in coms:
    rotate(xi, di, ki)
    board = find_near()

print(sum([sum(b) for b in board]))

# 2. 그 원판에 수가 있으면, 인접하면서 수가 같은 것을 찾는다.
# 찾고 나면 인접하면서 수 같은걸 모두 지운다.

# 3. 수가 만약 없으면 모든 원판 적힌 수의 평균을 구하고 크면 -1 작으면 +1 한다. 


