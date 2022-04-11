import time

# key = [[0,0,1,1],[1,0,1,1],[1,0,0,0],[0,0,0,0]]
# lock = [[0,0,1,1,1],[0,0,1,1,1],[1,1,1,1,1],[1,0,0,1,1],[1,1,1,1,1]]

# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
t0 = time.time()
key = [[0,0,0,1,1,1]]+[[0]*6 for _ in range(4)]+[[0,0,0,0,1,1]]

lock = [[0,0,1,1,1,1,1,1]+[1]*12]+[[1]*20 for _ in range(4)]\
+[[0,0,0,1,1,1,1,1]+[1]*12]+[[1]*20 for _ in range(14)]


n = len(lock)
m = len(key)

# key 회전
# 90
key_90 = [[0 for _ in range(len(key))] for _ in range(len(key))]
for x in range(len(key)):
    for y in range(len(key)):
        key_90[y][len(key)-(1+x)] = key[x][y]

# 180
key_180 = [[0 for _ in range(len(key))] for _ in range(len(key))]
for x in range(len(key)):
    for y in range(len(key)):
        key_180[y][len(key)-(1+x)] = key_90[x][y]

# 270
key_270 = [[0 for _ in range(len(key))] for _ in range(len(key))]
for x in range(len(key)):
    for y in range(len(key)):
        key_270[y][len(key)-(1+x)] = key_180[x][y]

key_rot = [key, key_90, key_180, key_270]


# key 이동 함수 구현
def move(dx, dy):    
    # dx, dy 만큼 옮겨서 값 넣기
    for x in range(len(key)): 
        for y in range(len(key)): 
            key_map[x+dx][y+dy] = key_rot[i][x][y]
            
    # if i == 2:
        # print(key_map)            
    

def check(dx,dy):
    # x, y 겹치는지 확인 - lock에 빈데가 있으면 다시 진행
    for x in range(dx, len(key)+dx):
        for y in range(dy, len(key)+dy):
            pos = (x,y)
            for lx in range(m-1, m-1+len(lock)):
                for ly in range(m-1, m-1+len(lock)):
                    lpos = (lx, ly)
                    # 겹치는 좌표 찾으면 - 0,1 반대되는지 확인
                    if lpos == pos:
                        
                        # key가 1, lock이 0이면 lock 을 1로 바꿈 (채우기)
                        if key_map[x][y] == 1 and lock_map[lx][ly] == 0:
                            lock_map[lx][ly] = 1
                        
                        elif key_map[x][y] == lock_map[lx][ly]: # 둘이 같은 경우 
                            return False # 키 안맞으므로 다시 move 해야함.

    # return 없이 겹치는부분을 채운경우 - 전체 lock이 1인지 확인
    for lx in range(m-1, m-1+len(lock)):
        for ly in range(m-1, m-1+len(lock)):
            if lock_map[lx][ly] != 1:
                return False
    
    return True



for i in range(len(key_rot)):    
    
    # key x로, y로 range(m+n-1)만큼 움직임
    for dx in range(m+n-1):
        for dy in range(m+n-1):

            # lock 재배치
            lock_map = [[-1 for _ in range(2*m+n-2)] for _ in range(2*m+n-2)]
            for x in range(len(lock)):
                for y in range(len(lock)):
                    lock_map[x+m-1][y+m-1] = lock[x][y]
            


            # key map 초기화
            key_map = [[-1 for _ in range(2*m+n-2)] for _ in range(2*m+n-2)]

            # key 이동
            move(dx, dy)
            # check 
            result = check(dx,dy)
            
            

            if result:
                print(i, dx, dy, True)
            # if i == 2 and dx == 5 and dy == 5:
            #     for z in lock_map:
            #         print(z)
            #     print('='*30)
            #     for l in key_map:
            #         print(l)
print(time.time() - t0)
print('program terminated.')
                
                
    
            
                    


                    

            