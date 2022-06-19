p = input()

# 올바른 괄호 문자열 판별
def correct(p):
    count = 0
    for ch in p:
        if ch == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False

# 균형잡힌 괄호 문자열 판별
def divide(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return p[:i+1], p[i+1:]

def solution(p):
    if correct(p):
        return p
    else:
        u, v = divide(p)
        if correct(u):
            return u + solution(v)
        else:
            ans = '('
            ans += solution(v)
            ans += ')'
            u = u[1:len(u)-1]
            for ch in u:
                if ch == '(':
                    ans += ')'
                elif ch == ')':
                    ans += '('
        return ans            
        


print(solution(p))


