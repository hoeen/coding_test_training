# ~6:30
n, m, h = map(int, input().split())
# n, m, h = 7, 1, 5
# n, m, h = 2, 1, 3
# n, m, h = 10, 1, 30
import time


lines = [[0]*(n-1) for _ in range(h)]   # h X n 
for _ in range(m):
    x, y = map(int, input().split())
    lines[x-1][y-1] = 1

# 도착 숫자 리턴하는 함수 구현
def arrive(lines):
    flist = list(range(1,n+1))
    # 매 가로줄마다 사다리 놓인 곳의 숫자를 바꿈
    for ix in range(h):
        for iy in range(n-1):
            if lines[ix][iy] == 1:
                flist[iy], flist[iy+1] = flist[iy+1], flist[iy]
    return flist

def check(lines, startx, starty, count): # startx, starty 처음에 0,0
    global max_count

    if m == 0:
        max_count = 0
        return
        
    if arrive(lines) == list(range(1,n+1)):
        print('found')
        time.sleep(1)
        if max_count == -1 or count < max_count: 
            max_count = count
        return

    if count == 3 or (0 < max_count <= count):
        return

    time.sleep(1)
    print('lines:')
    for l in lines:
        print(l)

    

    for x in range(max(0,startx), h):
        for y in range(n-1):
            if (x == startx and y < starty) or lines[x][y] == 1:
                continue
            else: # 비어있으면 - 주변 체크
                empty = True
                for i in range(2):
                    ny = y + dy[i]
                    if 0 <= ny < n-1:
                        if lines[x][ny] == 1: # 근처에 이미 놓아져 있으면
                            empty = False
                            break
                if empty:
                    # new_lines = [l[:] for l in lines]
                    lines[x][y] = 1
                    check(lines, x, y+2, count+1)
                    lines[x][y] = 0
    return 


dy = (-1,1)
max_count = -1
check(lines, -1, -1, 0)
print(max_count)
