A=int(input())
Array=list(map(int,input().split()))
unq_ele=[]
s=set()
for n in Array:
    if n not in s:
        unq_ele.append(n)
        s.add(n)
print(" ".join(map(str,unq_ele)))
