def ways(M):
    from math import factorial
    no_of_ways=factorial(M)
    return no_of_ways
M=int(input())
print(ways(M))
