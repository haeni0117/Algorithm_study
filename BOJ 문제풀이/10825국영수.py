import sys
num = int(input())
l = [map(input().split()).strip() for i in range(num)]#strip의 기능?
#이름이랑 점수는 자료형이 다른데 파라미터를 어떻게 2개를 쓰지? -> int or str인데 이게 가능한가?? 설마 for문으로?!
l.sorted(lambda x : x[3],x[2],x[1],x[0])
for i in l:
    print(i[0])