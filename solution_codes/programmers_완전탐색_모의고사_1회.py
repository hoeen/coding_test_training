# ~ 11:30
def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    pe1 = p1*(len(answers)//len(p1) + 1)
    pe2 = p2*(len(answers)//len(p2) + 1)
    pe3 = p3*(len(answers)//len(p3) + 1)
    
    pe1 = pe1[:len(answers)]
    pe2 = pe2[:len(answers)]
    pe3 = pe3[:len(answers)]
    
    cor = [0, 0, 0, 0]
    for i in range(len(answers)):
        if pe1[i] == answers[i]:
            cor[1] += 1
        if pe2[i] == answers[i]:
            cor[2] += 1
        if pe3[i] == answers[i]:
            cor[3] += 1
    result = []
    max_c = max(cor)
    for i in range(1, 4):
        if cor[i] == max_c:
            result.append(i)
    
    return result