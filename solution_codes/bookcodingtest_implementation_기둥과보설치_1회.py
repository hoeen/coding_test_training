# ~7:00
'''
기둥 보 : 길이 1인 선분
기둥 : 바닥위 or 보 한쪽끝위, 또는 다른기둥 위에만 존재
보 : 한쪽끝이 기둥위, 또는 양쪽끝부분이 다른 보와 연결.

삭제 : 여전히 규칙 만족해야함

build_frame: [x,y,a,b]
(x,y) 좌표, (0 기둥 1 보), (0 삭제 1 설치)


'''
# 걍 조건에 맞게 일일이 확인하면서 구현하면 될듯?
n = 0
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],
                [1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],
                [1,1,1,0],[2,2,0,1]]

# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# 정렬 문제같음..

# 1. build_frame을 x기준 정렬, -> y기준 정렬 -> 모두 같은 경우 0-1 정렬(기둥-보)
# 2. 설치와 삭제에서 조건을 만족하는지 확인하고 조건 안맞으면 삭제하기.
# 3. 1) 순서대로 build_frame을 따라가고, 설치삭제가 조건 만족하는지 보고 붙임.
# 4. 2) 끝까지 설치삭제 이루어졌으면, 정렬하면 끝.
def check(build):
    for x,y,a in build:
        if a == 0: # 기둥
            if y == 0 or [x-1, y, 1] in build or [x, y, 1] in build or [x,y-1,0] in build:
                continue
            return False
        elif a == 1: # 보 - 한쪽끝이 기둥위, 또는 양쪽끝부분이 다른 보와 연결.
            if [x, y-1, 0] in build or [x+1, y-1, 0] in build or ([x-1, y, 1] in build and [x, y, 1] in build):
                continue
            return False

    return True


def solution(n, build_frame):
    build_status = []
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b == 1: # 설치
            build_status.append([x,y,a])
            if check(build_status): # 잘 지어진경우
                pass
            else:
                build_status.remove([x,y,a])
        elif b == 0: # 제거
            build_status.remove([x,y,a])
            if check(build_status):
                pass
            else:
                build_status.append([x,y,a])

    return sorted(build_status)
            
print(solution(n,build_frame))