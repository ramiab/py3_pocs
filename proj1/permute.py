

def permute(l):
    if len(l) == 1:
        return [l]

    # print(l)
    tmp_res = []
    for c in l:
        l1 = list(l)
        l1.remove(c)
        p = permute(l1)
        for t in p:
            tmp_res.append([c]+ t )
    return tmp_res

l = list('abcd')
print( permute(l) )