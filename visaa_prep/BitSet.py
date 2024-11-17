Num=int(input())
L=int(input())
if Num & (1<<(L-1)) !=0:
    print("true")
else:
    print("false")
