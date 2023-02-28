def solution(sizes):
    max_h, max_v = 0, 0
    # 가로 < 세로로 맞춤
    for h, v in sizes:
        if h < v:
            h, v = v, h
        if max_h < h:
            max_h = h
        if max_v < v:
            max_v = v
            
    return max_h*max_v