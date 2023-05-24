from collections import defaultdict
import sys

sys.setrecursionlimit(int(1e8))

def solution(grid):
    '''
    모든 grid 에서 4방향으로 쏘기
    같은 사이클 판별? -> 처음 방향 처음 위치로 오면 길이 리턴
    같은 방향 하나라도 공유되면 같은 사이클이다
    '''
    dx = (-1, 0, 1, 0) # 12부터 시계방향
    dy = (0, 1, 0, -1)
    r, c = len(grid), len(grid[0])
    path_len_dict = {}
    memo = defaultdict(int)
    def recur(x, y, di, length, pnum):
        # memo exit
        if memo[(x, y, di)]: # 0 이상의 값을 가지면
            if memo[(x, y, di)] != pnum: # 이미 처리된 경로
                return # 길이 반환
            else: # 출발지로 돌아옴
                path_len_dict[pnum] = length
                return
        
        # exit 아니면 현재 경로를 저장
        memo[(x, y, di)] = pnum
        
        nx, ny = (x + dx[di]) % r, (y + dy[di]) % c
        if grid[nx][ny] == 'R':
            di = (di + 1) % 4
        elif grid[nx][ny] == 'L':
            di = (di - 1) % 4
        # s면 di 그대로
        recur(nx, ny, di, length + 1, pnum)
    
    path_num = 1
    for x in range(r):
        for y in range(c):
            for i in range(4):
                recur(x, y, i, 0, path_num)
                path_num += 1

    answer = []
    for key in path_len_dict.keys():
        answer.append(path_len_dict[key])
        
        
    return sorted(answer)