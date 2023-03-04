# Dictionaries in Python

str = [i.lower() for i in input('Input a words ').split()]

wrds = {w : str.count(w) for w in str}

for k, v in wrds.items():
    print('The word', k, 'in list is', v, 'times')
