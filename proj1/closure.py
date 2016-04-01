

def getFunc(multiplier):
    def getMultiplications(l):
        return [multiplier*i for i in l]
    return getMultiplications


funcs = []
for multiplier in range(4):
    funcs.append(getFunc(multiplier))

l = [10, 20, 30, 40, 50]
for f in funcs:
    print(f(l))