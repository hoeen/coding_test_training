def w(a, b, c, memo={}):
    # breakpoint()
    if (a,b,c) in memo:
        return memo[(a,b,c)]
    else:
        if a <= 0 or b <= 0 or c <= 0: 
            memo[(a,b,c)] = 1
            return 1

        elif a > 20 or b > 20 or c > 20: 
            if (20,20,20) in memo:
                memo[(a,b,c)] = memo[(20,20,20)]
            return w(20, 20, 20, memo)

        elif a < b and b < c: 
            if (a,b,c-1) in memo and\
                 (a,b-1,c-1) in memo and\
                    (a,b-1,c) in memo:
                memo[(a,b,c)] = memo[(a,b,c-1)] + memo[(a,b-1,c-1)] - memo[(a, b-1, c)]
            return w(a, b, c-1,memo) + w(a, b-1, c-1,memo) - w(a, b-1, c,memo)
        
        else:
            if (a-1,b,c) in memo\
                and (a-1,b-1,c) in memo\
                    and (a-1,b,c-1) in memo\
                        and (a-1,b-1,c-1) in memo:
                memo[(a,b,c)] = memo[(a-1, b, c)] + memo[(a-1, b-1, c)] + memo[(a-1, b, c-1)] - memo[(a-1, b-1, c-1)]
                
            return w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)


while True:
    a, b, c = map(int, input().split())
    if (a,b,c) == (-1,-1,-1):
        break
    print(f'w({a}, {b}, {c}) =', w(a,b,c))


