A,B,C=map(int,input().split())
time_req=A*B
avl_time=C*24*60
if time_req <= avl_time:
    print("YES")
else:
    print("NO")
