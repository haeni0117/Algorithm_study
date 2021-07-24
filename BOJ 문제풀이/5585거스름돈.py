money = 1000- int(input())
type = [500,100,50,10,5,1]
count = 0
for i in type :
    count += money//i
    money %=i
print(count)