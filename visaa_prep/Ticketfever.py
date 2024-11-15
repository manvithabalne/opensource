T=int(input())
for _ in range(0,T):
    K,L = map(int,input().split())
    if K>L:
        print(K-L)
    else:
        print("0")
