word = str(input())
_word = []
for i in range(len(word)) :
    _word.append(word[i:len(word)])
_word.sort()
for j in _word:
    print(j)