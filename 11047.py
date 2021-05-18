n,k=map(int,input().split())
#준규가 갖고 있는 동전의 종류(n)와 가치의 합(k)입력받기 => 최솟값구하기
#둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 
A=[]#동전의 가치를 입력받을 리스트
#동전의 종류 = number of 동전가치type
num = 0 #num = 동전의 개수
for i in range(n):
    A.append(int(input()))
for i in range(n-1,-1,-1):
    if k==0: #가치의 합이 0이라면 계산중지
        break
    if m[i]>k:
        continue #가장 가치가 큰 값부터 조사했을 때, k보다 크면 그 동전은 사용하지 못하므로 다른 동전(가치가 더 낮은)에 대해 조사해야함
    #이 두 경우에 해당되지 않는다면 -> m[i]인 동전으로 k를 구성할 수 있는 상황
    num += k//m[i]
    k %= m[i]
print(num)
//
n, k = map(int, input().split())
m = []
num = 0
for i in range(n):
    m.append(int(input()))
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if m[i] > k:
        continue
    num += k // m[i]
    k %= m[i]
print(num)