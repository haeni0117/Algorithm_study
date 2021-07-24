import sys
input = sys.stdin.readline
num = int(input())
_list = []
sum=0
for i in range(num):
    n=int(input())
    
    if n == 0:
        _list.pop()#틀린이유 0을 pop하는 게 아니라 0을 부르기 전의 수를 pop해야힌디/
    else:
        _list.append(n)
for number in _list:
    sum +=int(number)
print(sum)

        
        