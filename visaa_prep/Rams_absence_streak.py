def max_consec_absent_days(absnt):
    max_abs=0
    curr_abs=0
    for day in absnt:
        if day == 0:
            curr_abs+=1
            max_abs=max(max_abs,curr_abs)
        else:
            curr_abs=0
    return max_abs
Num=int(input())
absnt=list(map(int,input().split()))
print(max_consec_absent_days(absnt))
