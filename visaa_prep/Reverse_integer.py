n=int(input())
n_min= -2**31
n_max= 2**31 - 1
is_neg = n<0
rev=int(str(abs(n))[::-1])
if is_neg:
    rev=-rev
if rev < n_min or rev > n_max:
        print("0")
else:
        print(rev)
