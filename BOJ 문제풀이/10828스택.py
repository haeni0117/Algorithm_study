import sys
input = sys.stdin.readline
num = int(input())
stack = []
for i in range(num):
    command = input().split() #각각의 요소를 리스트로 받기
    if command[0]=="push":
        stack.append(command[1])
    elif command[0]=="pop":
        if len(stack)==0:
            print(-1)
        else : 
            print(stack[-1])
            stack.pop()
    elif command[0] == "size":
        print(len(stack))
    elif command[0]=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] =="top":
        if len(stack)==0:
            print(-1)
        else: 
            print(stack[-1])