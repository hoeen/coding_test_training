def solution(line):
    points = []
    # line 원소 중에 교점 생기는 경우 교점 정보 저장
    for i in range(len(line)-1):
        a, b, e = line[i]
        for j in range(i+1, len(line)):
            c, d, f = line[j]
            if a*d == b*c:
                continue
            else:
                p = (
                    (b*f - e*d) / (a*d - b*c),
                    (e*c - a*f) / (a*d - b*c)
                )
                if p[0]%1 == 0 and p[1]%1 == 0: # 정수 좌표일때
                    points.append(tuple(map(int, p)))
    
    # 저장된 정보들로 별을 나타내기
    # x 최소 최대 / y 최소 최대 찾기
    minx = min(points, key=lambda x: x[0])[0]
    maxx = max(points, key=lambda x: x[0])[0]
    miny = min(points, key=lambda x: x[1])[1]
    maxy = max(points, key=lambda x: x[1])[1]
    
    # x 최소 , y 최소를 0으로 하고 그만큼 모든 점들을 이동
    new_points = []
    for nx, ny in points:
        new_points.append((nx-minx, ny-miny))
    
    # x 최대 - 최소  / y 최대 - 최소 길이의 배열을 정의하여 모든 포인트를 *로 넣기
    lenx = maxx - minx + 1
    leny = maxy - miny + 1
    # print('new_p')
    # print(new_points)
    answer = [['.']*(lenx) for _ in range(leny)]
    for nx, ny in new_points:
        answer[leny-1-ny][nx] = '*'
    
    new_answer = []
    for a in answer:
        new_answer.append(''.join(a))
    
    return new_answer