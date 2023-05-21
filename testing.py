# 3 = 3 x 2 x 1 x -10

def Calculate(Number):
    Result = -10
    for i in range(1, Number + 1):
        Result = Result * i
    return Result


print(Calculate(3))
