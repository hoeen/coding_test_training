# 시작시간 7시
# ~9:10
'''
거리두기
파티션 막혀 있으면 상관없음
안막혀 있으면, 거리가 2보다 커야함

풀이?
응시자를 찾고,
응시자별 맨해튼 거리 2 내에서 다른 사람 탐색
다른 사람 있으면 - 거리 1이면 탈락, 2이면 x,y중 같으면 사이에 파티션, 대각선이면 나머지공간 파티션 탐색

'''
dx = (-1,1,0,0) # 상하좌우
dy = (0,0,-1,1)
d2x = (-2, -1, 0, 1, 2, 1, 0, 1) # 위부터 시계방향
d2y = (0, 1, 2, 1, 0, -1, -2, -1)
def corona(room):
    for x in range(5):
        for y in range(5):
            if room[x][y] == 'P':
                # print('found:', (x,y))
                # 주위 응시자 찾기 - 거리 1
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if (0 <= nx < 5) and (0 <= ny < 5):
                        if room[nx][ny] == 'P':
                            return False
                # 주위 응시자 찾기 - 거리 2
                for i in range(8):
                    rx, ry = x + d2x[i], y + d2y[i]
                    if (0 <= rx < 5) and (0 <= ry < 5):
                        # print(rx,ry)
                        
                        if room[rx][ry] == 'P':
                            # print('dist2:', (rx, y+d2y[i]//2), (rx+d2x[i]//2, ry) )
                            # x 같거나 y 같은경우 - 사이 파티션 여부
                            if x == rx:
                                if room[rx][y+d2y[i]//2] != 'X':
                                    return False
                            elif y == ry:
                                if room[x+d2x[i]//2][ry] != 'X':
                                    return False
                            # x y 다 다른경우 : 파티션 2개 여부
                            else:
                                if room[rx][y] != 'X' or room[x][ry] != 'X':
                                    return False
    return True


                
                


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result = []
for room in places:
    # print(corona(room))
    if corona(room):
        result.append(1)
    else:
        result.append(0)

print(result)