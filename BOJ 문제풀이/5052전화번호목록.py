def fct():
    for i in range(a-1):
        if _list[i]==_list[i+1][0:len(_list[i])]:
            print("NO");
            return
    print("YES")

n = int(input())

for i in range(n):
    a = int(input())
    _list = []
    for _ in range(a):
        _list.append(input().strip())
    _list.sort() #순서대로 정렬
    fct()  