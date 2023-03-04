# Determine polindrom

word = input('Input the word:\n\t')

if word == word[:: -1]:
    print('Word is polindrom')
else:
    print('Word is not polindrom')
