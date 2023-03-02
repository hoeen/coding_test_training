def solution(brown, yellow):
    answer = [] 
    total = brown + yellow
    for hor in range(1, total//2): # 가로 기준 진행
        if total % hor != 0 or total // hor > hor:
            continue
        ver = total // hor
        check_brown = 2*(hor + ver - 2)  # 갈색 노란색 개수 확인
        check_yellow = total - check_brown
        if brown == check_brown and yellow == check_yellow:
            return [hor, ver]