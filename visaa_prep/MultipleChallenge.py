def div(K):
    count_3=n//3
    count_5=n//5
    count_15=n//15
    ttl_count=count_3 + count_5 - count_15
    return ttl_count
n=int(input())
result =div(n)
print(result)
