import re

S = "test 5 a0A pass007 ?xy1 ?##pass007!#"
def solution(S):
    for word in sorted(S.split(' '), key=lambda x: len(x), reverse=True):
        if len(re.compile('[^a-zA-Z0-9]').findall(word)) > 0:
            continue
        alplen = len(re.compile('[a-zA-z]').findall(word))
        numlen = len(re.compile('[0-9]').findall(word))
        if alplen%2 == 0 and numlen%2 == 1:
            return len(word)
    
    return -1

print(solution(S))