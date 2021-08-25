ascending = True
descending = True
num = list(map(int,input().split()))
for i in range(7):
    if num[i]>num[i+1]:
        ascending=False
    if num[i]<num[i+1]:
        descending = False
if ascending :
    print('ascending')
elif descending :
    print('descending')
else :
    print('mixed')