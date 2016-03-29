def fibo(size):
    '''0, 1, 1, 2, 3, 5, 8, 13'''
    res = [0, 1]
    for i in range(size - 2):
        res.append(sum(res[i:]))

    return res

print( fibo(8) )