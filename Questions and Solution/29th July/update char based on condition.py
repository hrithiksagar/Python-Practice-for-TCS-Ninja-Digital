word1 = input()#Enter word1
word2 = input()#Enter word2
word3 = input()#Enter word3
vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
for i in range(len(word1)):
    if word1[i] in vowels:
        word1 = word1.replace(word1[i], '%')
for i in range(len(word2)):
    if word2[i] not in vowels:
        word2 = word2.replace(word2[i], '#')
for i in range(len(word3)):
    if i%2==0:
        word3 = word3.replace(word3[i], word3[i].lower())
    else:
        word3 = word3.replace(word3[i], word3[i].upper())
print(word1+word2+word3)