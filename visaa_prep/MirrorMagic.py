num=int(input())
mir_matrix=[]
for _ in range(num):
    row=list(map(int,input().strip().split()))
    mir_matrix=row[::-1]
    print(" ".join(map(str, mir_matrix)))
