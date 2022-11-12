def perm(input_list, n):
    result = []
    if len(input_list) < n:
        return result
    elif n == 1:
        for i in input_list:
            result.append([i])
    elif n > 1:
        for j in range(len(input_list)):
            temp = [k for k in input_list]
            temp.remove(input_list[j])
            for p in perm(temp, n-1):
                result.append([input_list[j]] + p)
    return result    



print(perm([1,2,3,4], 3))