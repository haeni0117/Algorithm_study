#1st
n = int(input())
num_list = list(map(int,input().split()))
#중복허용아닌걸 알 수 있음 -> example2
num_list2=list(set(num_list)) #중복제거
#문제가 뭔소린지...
#수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
#okay 이해했음
for i in range(len(num_list2)):
    cnt=0
    for j in range(len(num_list2)):
        if num_list2[i]>num_list2[j] :
            cnt+=1
            #문제! 어떻게 다시 원래 리스트에 집어넣을까...?
        for k in range(n):
            if num_list[k]==num_list2[i]:
                num_list[k].append(cnt)

for i in range(n):
    print(num_list[i][1],end=" ")  
        

#2nd
n = int(input())
num_list = map(int,input().split())
num_list3 = []
#중복허용아닌걸 알 수 있음 -> example2
num_list2=list(set(num_list)) #중복제거
#문제가 뭔소린지...
#수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
#okay 이해했음
for i in range(len(num_list2)):
    cnt=0
    for j in range(len(num_list2)):
        if num_list2[i]>num_list2[j] :
            cnt+=1
            #문제! 어떻게 다시 원래 리스트에 집어넣을까...?
        for k in range(n):
            if num_list[k]==num_list2[i]:
                num_list3.append((num_list[k],cnt))

for i in range(n):
    print(num_list3[i][1],end=" ")  