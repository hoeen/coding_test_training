# board = [list(map(int, input().split())) for _ in range(10)]
import time

papers = [0, 5, 5, 5, 5, 5]
result = set() # 자동 중복 방지

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


def find_length(y, x):
    length = 1
    for l in range(2, min(10 - y, 10 - x, 5) + 1):
        for i in range(y, y+l):
            for j in range(x, x+l):
                if board[i][j] == 0:
                    return length # 1이 아니면 최대 범위로 설정
        length += 1
    return length

def cover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            board[i][j] = 0

def uncover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            board[i][j] = 1

def dfs(cnt):

    for i in range(0, 10):
        for j in range(0, 10):
            if board[i][j] == 1:
                length = find_length(i, j)
                for l in range(length, 0, -1):
                    if papers[l]:
                        cover(i, j, l)
                        papers[l] -= 1

                        time.sleep(0.5)
                        print('check')
                        for b in board:
                            print(b)
                        print(papers)
                        


                        result.add(dfs(cnt + 1))
                        uncover(i, j, l)
                        papers[l] += 1 
                if result:
                    return min(result)
                else:
                    return -1
    return cnt

result.add(dfs(0))
if -1 in result:
    result.remove(-1)
print(min(result) if result else -1)