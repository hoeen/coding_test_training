# ~ 5:40
'''
0 빈칸 / 1 벽 / 2 바이러스
벽은 무조건 세개만 . 
이때 0의 개수의 최댓값을 구하시오.
'''
# 1을 임의로 세 곳에 세웠을때, 모든 장소에 바이러스 퍼뜨리고, 남은곳을 0으로 해서 카운트하자.
# 조합 이용 - 최대 64C3
# 1. 0 중에 세곳 골라서 1로 만든다
# 2. BFS로 2를 마구 퍼뜨린다!
# 3. 남은 0 개수를 센다
# 4. 0의 최댓값을 출력한다.
import copy 

def comb(input_list, n):
    ret = []
    # 1. exit
    if len(input_list) < n:
        return ret
    # 2.
    elif n == 1:
        for i in input_list:
            ret.append([i])

    # 3.
    else:
        temp = [k for k in input_list]
        for j in range(len(input_list)):
            temp.remove(input_list[j])
            for c in comb(temp, n-1):
                ret.append([input_list[j]] + c)

    return ret

def find(sci):
    zero = []
    virus = []
    for row in range(n):
        for col in range(m):
            if sci[row][col] == 0:
                zero.append((row,col))
            elif sci[row][col] == 2:
                virus.append((row,col))  
    return zero, virus #0의위치 찾아서 리스트로 반환

def execute(sci, case):
    
    temp = copy.deepcopy(sci)

    def bfs(row,col):
        dx = (-1,0,1,0)
        dy = (0,-1,0,1)
    
        if temp[row][col] == 0:
            temp[row][col] = 2
            # print('infected', (row,col))
        
        for i in range(4):
            if row+dx[i] >= 0 and row+dx[i] < n and col+dy[i] >= 0 and col+dy[i] < m:
                if temp[row+dx[i]][col+dy[i]] == 0:
                    # print('move', dx[i], dy[i])
                    bfs(row+dx[i],col+dy[i])
            
        return 
    
    
    
 
    for i in range(3):
        temp[case[i][0]][case[i][1]] = 1 # 벽 세우기 
    
    for vx, vy in virus:
        bfs(vx,vy)
    # count 0
    zero_found, _ = find(temp)
    
    
    return len(zero_found)
    
n,m = map(int, input().split())  # 세로, 가로


lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

zero, virus = find(lab)

zero_comb = comb(zero, 3)  # 3개 고른 리스트

cand_list = []

for case in zero_comb: # [(1, 4), (3, 0), (3, 3)]= case
    cand_list.append(execute(lab, case))
    
    
print(max(cand_list))





