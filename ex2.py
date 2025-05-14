text=input().strip()
listtext=list(text.lower())
vowels=0
vowels=vowels+listtext.count('e')+listtext.count('a')+listtext.count('o')+listtext.count('u')+listtext.count('i')
print(vowels)