P, Q=map(int,input().split())
Arr=map(int,input().split())
even_sum=0
odd_sum=0
for i in Arr:
    if i%Q==0:
        even_sum += i
    else:
        odd_sum += i
print(even_sum - odd_sum)
