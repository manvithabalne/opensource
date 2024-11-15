A,B,C = map(int, input().split())
Max_Mangoes_Weight=C - B
if Max_Mangoes_Weight <= 0:
    Max_Mangoes = 0
else:
    Max_Mangoes=Max_Mangoes_Weight // A
print(Max_Mangoes)
