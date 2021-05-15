def waysToTraverse(width,height):
    x_distance = width - 1
    y_distance = height - 1

    numerator = factorial(x_distance,y_distance)
    denominator = factorial(x_distance)*factorial(y_distance)

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res
    
