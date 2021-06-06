n = int(input())
words=[]
word={}
for i in range(n):
    word.add(i)
for j in range(len):
    w = list(input())#문자열(단어)그 자체를 리스트로
    w.append(len(w))#글자길이를 [i][1]에 넣는다.
    words.append(w)
words.sort(key=lambda x :(x[1],x[0]))#이러면 알파벳 순?
for i in range(len(words)):
    print(words[i][0])

#문제점
#1집합은 어떻게 모든 요소를 조사하는가 cf 리스트를 for i in range사용
#2문자열의 길이에 따라 나열하는 것은 할 수 있음 but 사전순정렬은 how?