# Cycles and strings in Python
# remove every even character

str1 = input('Input the word ')
str2 = ''

for i in range(0, len(str1), 2):
    str2 += str1[i]

print(str2)
