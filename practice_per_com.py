def perm(input_list, n):
    result = []
    # 1.
    if len(input_list) < n:
        return result

    # 2.
    elif n == 1:
        for i in input_list:
            result.append([i])

    # 3.
    else:
        for k in range(len(input_list)):
            temp = [j for j in input_list]
            temp.remove(input_list[k])
            for p in perm(temp, n-1):
                result.append([input_list[k]] + p)

    return result

print(perm([1,2,3,4],3))