num1,num2 = map(int,input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
answer_list = list1+list2
answer = ' '.join(map(str, sorted(answer_list)))
# '구분자'.join(리스트) -> 리스트를 합쳐주는 역할이라고 생각하면 되겠다.
# '구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
# '_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

# 출처: https://blockdmask.tistory.com/468 [개발자 지망생]
print(answer)
  