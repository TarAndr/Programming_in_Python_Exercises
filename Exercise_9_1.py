# Cycles and strings in Python
# insert space between characters

str1 = input('Input the word ')
str2 = ''

for i in range(len(str1)):
    str2 += str1[i] + ' '

print(str2)
