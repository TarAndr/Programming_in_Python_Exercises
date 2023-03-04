# Swap the halfs of string

text = input('Input the word:\n\t')

swappedText = text[(len(text) + 1) // 2 :] + text[: (len(text) + 1) // 2]

print(swappedText)
