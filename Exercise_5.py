# Strings in Python

a = 'String'
b = "String 1"

print(a, b)

c = a + b
print(c)

print(a * 4)

print(a in b)

# Escapes
# \n \t 

# Compare
str1 = '1a'
str2 = 'Aa'
str3 = 'aa'
print(str1 < str2)
print(str2 < str3)

print(str2.lower())
print(str2.upper())
print(str3.capitalize())

str4 = 'hello, world!'
print(str4.title())

print(len(str4))
print(str4[-1], str4[0], str4[12])
print(str4[3 : 7])
print(str4[: 3])
print(str4[7 :])
print(str4[-9 : -5])
print(str4[ : : 2])


str4 = str4.replace('o', '@')
print(str4)
