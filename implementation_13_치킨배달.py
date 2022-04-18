# ~9:50
n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 조합 구현 - 전체에서 m개를 조합으로 뽑는 경우의 수
def comb(input_list, n):
    result = []
    if len(input_list) < n:
        return result

    elif n == 1:
        for i in input_list:
            result.append([i])
    
    else:
        temp = [j for j in input_list]
        for k in range(len(input_list)):
            temp.remove(input_list[k])
            for p in comb(temp, n-1):
                result.append([input_list[k]] + p)
    
    return result

# print(board)

# 칰 위치 찾는 함수
def find_chick_and_house():
    chick = []
    house = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 2:
                chick.append((row,col))
            elif board[row][col] == 1:
                house.append((row,col))
    return house, chick


# 칰 거리 구하는 함수
def dist_chick(house, chick):
    sum_dist = 0
    for x, y in house:
        dist_one_list = []
        for xc, yc in chick:
            dist_one_list.append(abs(x-xc) + abs(y-yc))
        sum_dist += min(dist_one_list)

    return sum_dist       

# 치킨 및 집 위치 저장
house, chick = find_chick_and_house()

# m개만큼 치킨집 뽑음
chick_case_list = comb(chick, m)

# m개 뽑는 경우의 수에서 각각 치킨거리 구함
chick_dist_list = []
for i in range(len(chick_case_list)):
    chick_dist_list.append(dist_chick(house, chick_case_list[i]))

# print(chick_dist_list)
print(min(chick_dist_list))
    



# print(comb([(2,3),(3,2),(4,1)], 3))
