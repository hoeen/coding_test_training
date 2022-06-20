# ~10:50  ~ 11:10
'''
S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오.
'''
from collections import deque

n, k = map(int, input().split()) # 1~k까지의 바이러스 숫자 부여

flask = []
for _ in range(n):
    flask.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

# 초마다, 모든 바이러스에 대해서 숫자 순서대로 상하좌우를 살핀다.
# 숫자 순서로 공백을 채워넣는다.
loc_list = [[] for _ in range(k+1)] # 1~k 각각의 정보


qlist = []
for row in range(n):
    for col in range(n):
        if flask[row][col] != 0:
            
            qlist.append((flask[row][col],row,col))
            qlist = sorted(qlist, key=lambda x: x[0])
q = deque(qlist)  # 1~k순서로 들어감

'''
방문 만들기.
방문 안했으면 방문처리.
근데 어떻게 순서대로 1,2,3?
옆에 비어있을때 한번씩만 채운다.
'''
dx = (-1,0,1,0)
dy = (0,-1,0,1)



for _ in range(s):
    for _ in range(len(q)):
        num, qx, qy = q.popleft()
        # 상하좌우 조사
        for i in range(4):
            nx, ny = qx+dx[i], qy+dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if flask[nx][ny] == 0:
                    flask[nx][ny] = num
                    q.append((num,nx,ny))
    
    
print(flask[x-1][y-1])  

    