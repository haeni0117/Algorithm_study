import random 
def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        
        if swap == False:
            break
    return data

def _bubblesort(data):
    for index in range(len(data)-1):
      swap = False
      for index2 in range(len(data)-index-2):
      
        if data[index2] > data[index2+1]:
            data[index2],data[index2+1]=data[index2+1],data[index2] #swap
            swap=True #swap이 한 번이라도 일어나면 변수 swap의 값은 true가 된다.
      if swap == False:#턴을 돌렸음에도 swap이 일어나지 않았다면?
          break
    return data
      

## 직접 정렬알고리즘을 사용해서 정렬해보자!


data_list = random.sample(range(100),50)#1~100까지의 랜덤샘플 50개
print(bubblesort(data_list))
print(_bubblesort(data_list))